"""ALS model wrapper using implicit library.

TODO (M2): Implement full ALS training and inference.
"""


class ALSModel:
    """Alternating Least Squares collaborative filtering model."""

    def __init__(self, model_path: str | None = None):
        self.model = None
        self.version = "v0.1"
        if model_path:
            self.load(model_path)

    def load(self, path: str):
        """Load a trained ALS model from disk."""
        # TODO: Load pickle/npy artifacts
        pass

    def predict(self, user_id: int, k: int = 20) -> list[int]:
        """Generate top-K recommendations for a user.

        Args:
            user_id: Target user ID.
            k: Number of recommendations.

        Returns:
            List of recommended movie IDs.
        """
        # TODO: Real inference
        return [50, 172, 1, 318, 296][:k]
