"""Probe script — periodically hits /recommend and logs to Kafka.

Intended to run as a GitHub Actions cron job.

TODO (M2): Full implementation with Kafka producer for reco_requests/reco_responses.

Usage:
    python scripts/probe.py --api-url https://your-service.run.app --user-ids 1,2,3,4,5
"""

import argparse
import os
import time
import requests


def probe(api_url: str, user_ids: list[int], k: int = 20):
    """Hit the /recommend endpoint and record results.

    Args:
        api_url: Base URL of the deployed API.
        user_ids: List of user IDs to probe.
        k: Number of recommendations to request.
    """
    results = []
    for uid in user_ids:
        url = f"{api_url}/recommend/{uid}?k={k}"
        start = time.time()
        try:
            resp = requests.get(url, timeout=5)
            latency = time.time() - start
            results.append({
                "user_id": uid,
                "status": resp.status_code,
                "latency_ms": round(latency * 1000, 1),
                "recommendations": resp.text if resp.ok else None,
                "timestamp": int(time.time()),
            })
            print(f"  user={uid} status={resp.status_code} latency={latency*1000:.1f}ms")
        except Exception as e:
            print(f"  user={uid} ERROR: {e}")
            results.append({"user_id": uid, "status": 0, "error": str(e)})

    # TODO (M2): Write results to {team}.reco_requests and {team}.reco_responses Kafka topics

    success = sum(1 for r in results if r.get("status") == 200)
    print(f"\nProbe complete: {success}/{len(results)} successful")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Probe the recommendation API")
    parser.add_argument("--api-url", default=os.getenv("API_URL", "http://localhost:8000"))
    parser.add_argument("--user-ids", default="1,2,3,4,5,10,50,100,500,1000")
    parser.add_argument("--k", type=int, default=20)
    args = parser.parse_args()
    ids = [int(x) for x in args.user_ids.split(",")]
    probe(args.api_url, ids, args.k)
