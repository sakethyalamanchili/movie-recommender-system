"""Tests for model inference wrappers."""

from service.models import ALSModel, NCFModel


def test_als_predict_returns_list():
    """ALS predict returns a list of movie IDs."""
    model = ALSModel()
    result = model.predict(user_id=1, k=5)
    assert isinstance(result, list)
    assert len(result) == 5
    assert all(isinstance(x, int) for x in result)


def test_ncf_predict_returns_list():
    """NCF predict returns a list of movie IDs."""
    model = NCFModel()
    result = model.predict(user_id=1, k=5)
    assert isinstance(result, list)
    assert len(result) == 5
    assert all(isinstance(x, int) for x in result)
