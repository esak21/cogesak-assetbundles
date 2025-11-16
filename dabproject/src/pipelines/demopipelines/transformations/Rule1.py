import dlt 



@dlt.table()
def bronze_transform():
    return spark.range(10)