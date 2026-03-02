"""Tests for Kafka consumer and schema validation.

TODO (M2): Add integration tests once Kafka is wired.
"""

from stream.schemas.events import watch_schema, rate_schema
import pandas as pd


def test_watch_schema_valid():
    """Valid watch event passes schema."""
    df = pd.DataFrame([{"user_id": 1, "movie_id": 50, "timestamp": 1700000000}])
    validated = watch_schema.validate(df)
    assert len(validated) == 1


def test_rate_schema_valid():
    """Valid rate event passes schema."""
    df = pd.DataFrame([{"user_id": 1, "movie_id": 50, "rating": 4.5, "timestamp": 1700000000}])
    validated = rate_schema.validate(df)
    assert len(validated) == 1


def test_rate_schema_invalid_rating():
    """Rating outside 0.5-5.0 fails schema."""
    import pandera
    df = pd.DataFrame([{"user_id": 1, "movie_id": 50, "rating": 6.0, "timestamp": 1700000000}])
    try:
        rate_schema.validate(df)
        assert False, "Should have raised SchemaError"
    except pandera.errors.SchemaError:
        pass
