"""Offline evaluation: HR@K and NDCG@K.

TODO (M2/M3): Full implementation with chronological split.

Usage:
    python -m training.evaluate --model-path /model_registry/v1.0/ --data-path /snapshots/latest/
"""

import argparse
import json


def hit_rate_at_k(recommended: list[list[int]], actual: list[int], k: int = 10) -> float:
    """Compute Hit Rate @ K."""
    hits = sum(1 for recs, true_id in zip(recommended, actual) if true_id in recs[:k])
    return hits / len(actual) if actual else 0.0


def ndcg_at_k(recommended: list[list[int]], actual: list[int], k: int = 10) -> float:
    """Compute NDCG @ K."""
    import math
    ndcg = 0.0
    for recs, true_id in zip(recommended, actual):
        if true_id in recs[:k]:
            rank = recs[:k].index(true_id) + 1
            ndcg += 1.0 / math.log2(rank + 1)
    return ndcg / len(actual) if actual else 0.0


def evaluate(model_path: str, data_path: str, k: int = 10):
    """Run offline evaluation and save results.

    Args:
        model_path: Path to model artifacts.
        data_path: Path to test data snapshot.
        k: Cutoff for ranking metrics.
    """
    # TODO (M2/M3):
    # 1. Load test split
    # 2. Generate predictions for each test user
    # 3. Compute HR@K and NDCG@K
    # 4. Save eval_report.json
    print(f"Evaluating: model={model_path}, data={data_path}, k={k}")

    results = {
        "model_path": model_path,
        "data_path": data_path,
        "k": k,
        "hr_at_k": 0.0,    # TODO: compute
        "ndcg_at_k": 0.0,  # TODO: compute
    }
    print(json.dumps(results, indent=2))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate model offline")
    parser.add_argument("--model-path", required=True)
    parser.add_argument("--data-path", required=True)
    parser.add_argument("--k", type=int, default=10)
    args = parser.parse_args()
    evaluate(args.model_path, args.data_path, args.k)
