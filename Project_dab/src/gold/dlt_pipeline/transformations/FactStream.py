import dlt
from pyspark.sql.functions import col

@dlt.table
def FactStream_stg():
    return spark.readStream.table("project_catalog.silver.FactStream")

dlt.create_streaming_table("FactStream")

dlt.create_auto_cdc_flow(
    target="FactStream",
    source="FactStream_stg",
    keys=["stream_id"],
    sequence_by=col("stream_timestamp"),
    stored_as_scd_type=1
)