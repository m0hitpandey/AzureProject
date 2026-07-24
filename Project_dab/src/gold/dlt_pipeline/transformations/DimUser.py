import dlt
from pyspark.sql.functions import col

expect = {

    "rule_1" : "user_id IS NOT NULL"
}

@dlt.table
@dlt.expect_all_or_drop(expect)
def userstg():
    return spark.readStream.table("project_catalog.silver.dimuser")

dlt.create_streaming_table(
    name = "dimuser" ,
    expect_all_or_drop = expect
    )

dlt.create_auto_cdc_flow(
    target="dimuser",
    source="userstg",
    keys=["user_id"],
    sequence_by=col("updated_at"),
    stored_as_scd_type=2
)