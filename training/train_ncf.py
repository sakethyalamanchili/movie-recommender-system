"""Train NCF (NeuMF) model on MovieLens-1M.

TODO (M2): Full implementation.

Usage:
    python -m training.train_ncf --data-path /snapshots/latest/ --output /model_registry/v1.1/
"""

import argparse


def train_ncf(data_path: str, output_path: str, embed_dim: int = 64,
              mlp_layers: str = "128,64,32", epochs: int = 30, lr: float = 0.001):
    """Train a NeuMF model using PyTorch.

    Args:
        data_path: Path to the Parquet data snapshot.
        output_path: Path to save model artifacts.
        embed_dim: Embedding dimension for user/item.
        mlp_layers: Comma-separated MLP layer sizes.
        epochs: Max training epochs (early stopping applied).
        lr: Learning rate.
    """
    # TODO (M2):
    # 1. Load Parquet snapshot
    # 2. Build train/val datasets with negative sampling
    # 3. Define NeuMF architecture (GMF + MLP paths)
    # 4. Train with BCE loss + Adam + early stopping
    # 5. Save .pt model + metadata.json
    layers = [int(x) for x in mlp_layers.split(",")]
    print(f"Training NCF: data={data_path}, output={output_path}")
    print(f"Hyperparams: embed_dim={embed_dim}, layers={layers}, epochs={epochs}, lr={lr}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train NCF model")
    parser.add_argument("--data-path", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--embed-dim", type=int, default=64)
    parser.add_argument("--mlp-layers", default="128,64,32")
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--lr", type=float, default=0.001)
    args = parser.parse_args()
    train_ncf(args.data_path, args.output, args.embed_dim, args.mlp_layers, args.epochs, args.lr)
