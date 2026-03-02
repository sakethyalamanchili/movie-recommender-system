"""Recommender API — FastAPI service with Prometheus metrics."""

import os
import time
from fastapi import FastAPI, HTTPException, Header
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(title="Movie Recommender API", version="0.1.0")

# ── Prometheus Metrics ──
REQUEST_COUNT = Counter(
    "recommend_requests_total",
    "Total recommendation requests",
    ["status"]
)
REQUEST_LATENCY = Histogram(
    "recommend_latency_seconds",
    "Recommendation request latency",
    buckets=[0.01, 0.025, 0.05, 0.1, 0.2, 0.5, 1.0]
)

# ── Model state ──
CURRENT_MODEL = os.getenv("MODEL_VERSION", "v0.1")


@app.get("/healthz")
def healthz():
    """Liveness probe."""
    return {"status": "ok", "model_version": CURRENT_MODEL}


@app.get("/recommend/{user_id}")
def recommend(user_id: int, k: int = 20, model: str | None = None):
    """Return top-K movie recommendations for a user.

    Args:
        user_id: The user to generate recommendations for.
        k: Number of recommendations to return (default 20).
        model: Optional model version override for A/B testing.

    Returns:
        Comma-separated string of movie IDs.
    """
    start = time.time()
    try:
        # TODO: Replace with real model inference in M2
        # Placeholder: return popular movie IDs
        popular_ids = [50, 172, 1, 318, 296, 593, 260, 480, 527, 110,
                       589, 2571, 1270, 2762, 1580, 1210, 2028, 357, 588, 1197]
        recommendations = popular_ids[:k]

        REQUEST_COUNT.labels(status="200").inc()
        latency = time.time() - start
        REQUEST_LATENCY.observe(latency)

        return ",".join(map(str, recommendations))

    except Exception as e:
        REQUEST_COUNT.labels(status="500").inc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/switch")
def switch_model(model: str, authorization: str = Header(None)):
    """Hot-swap the active model version (admin-only).

    Args:
        model: Model version string (e.g., 'v1.2').
        authorization: Bearer token for admin access.
    """
    global CURRENT_MODEL
    admin_token = os.getenv("ADMIN_TOKEN", "")

    if not authorization or authorization != f"Bearer {admin_token}":
        raise HTTPException(status_code=403, detail="Unauthorized")

    old_version = CURRENT_MODEL
    # TODO: Actually load new model artifacts in M2
    CURRENT_MODEL = model

    return {
        "status": "switched",
        "old_version": old_version,
        "new_version": model
    }


@app.get("/metrics")
def metrics():
    """Prometheus metrics endpoint."""
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
