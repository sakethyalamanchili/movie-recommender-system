"""Neural Collaborative Filtering (NeuMF) model wrapper.

TODO (M2): Implement full NCF architecture and inference.
"""


class NCFModel:
    """Neural Collaborative Filtering combining GMF + MLP paths."""

    def __init__(self, model_path: str | None = None):
        self.model = None
        self.version = "v0.1"
        if model_path:
            self.load(model_path)

    def load(self, path: str):
        """Load a trained NCF model from disk.

        Args:
            path: Path to the .pt model file.
        """
        # TODO: Load PyTorch model
        pass

    def predict(self, user_id: int, k: int = 20) -> list[int]:
        """Generate top-K recommendations for a user.

        Args:
            user_id: Target user ID.
            k: Number of recommendations.

        Returns:
            List of recommended movie IDs.
        """
        # TODO: Real inference with torch.no_grad()
        return [50, 172, 1, 318, 296][:k]
