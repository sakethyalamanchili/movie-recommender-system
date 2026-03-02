"""Train ALS baseline model on MovieLens-1M.

TODO (M2): Full implementation.

Usage:
    python -m training.train_als --data-path /snapshots/latest/ --output /model_registry/v1.0/
"""

import argparse


def train_als(data_path: str, output_path: str, factors: int = 64, iterations: int = 15):
    """Train an ALS model using the implicit library.

    Args:
        data_path: Path to the Parquet data snapshot.
        output_path: Path to save model artifacts.
        factors: Number of latent factors.
        iterations: Number of ALS iterations.
    """
    # TODO (M2):
    # 1. Load Parquet snapshot
    # 2. Build user-item sparse matrix
    # 3. Train implicit.als.AlternatingLeastSquares
    # 4. Save model + metadata.json
    print(f"Training ALS: data={data_path}, output={output_path}")
    print(f"Hyperparams: factors={factors}, iterations={iterations}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train ALS model")
    parser.add_argument("--data-path", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--factors", type=int, default=64)
    parser.add_argument("--iterations", type=int, default=15)
    args = parser.parse_args()
    train_als(args.data_path, args.output, args.factors, args.iterations)
