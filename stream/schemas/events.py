"""Event schema definitions using pandera.

TODO (M2): Define full Avro schemas for Schema Registry integration.
"""

import pandera as pa
from pandera import Column, Check

# Schema for watch events
watch_schema = pa.DataFrameSchema({
    "user_id": Column(int, Check.gt(0), nullable=False),
    "movie_id": Column(int, Check.gt(0), nullable=False),
    "timestamp": Column(int, Check.gt(0), nullable=False),
})

# Schema for rating events
rate_schema = pa.DataFrameSchema({
    "user_id": Column(int, Check.gt(0), nullable=False),
    "movie_id": Column(int, Check.gt(0), nullable=False),
    "rating": Column(float, Check.in_range(0.5, 5.0), nullable=False),
    "timestamp": Column(int, Check.gt(0), nullable=False),
})
