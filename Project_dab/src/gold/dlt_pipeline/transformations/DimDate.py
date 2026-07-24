import dlt
from pyspark.sql.functions import col

@dlt.table
def datestg():
    return spark.readStream.table("project_catalog.silver.dimdate")

dlt.create_streaming_table("dimdate")

dlt.create_auto_cdc_flow(
    target="dimdate",
    source="datestg",
    keys=["date_key"],
    sequence_by=col("date"),
    stored_as_scd_type=2
)