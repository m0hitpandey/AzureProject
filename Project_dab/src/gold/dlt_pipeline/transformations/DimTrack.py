import dlt
from pyspark.sql.functions import col

@dlt.table
def trackstg():
    return spark.readStream.table("project_catalog.silver.dimtrack")

dlt.create_streaming_table("dimtrack")

dlt.create_auto_cdc_flow(
    target="dimtrack",
    source="trackstg",
    keys=["track_id"],
    sequence_by=col("updated_at"),
    stored_as_scd_type=2
)