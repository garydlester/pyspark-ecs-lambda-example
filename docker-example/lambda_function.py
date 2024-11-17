from pyspark.sql import SparkSession
from commonlib import test as t1
from gmcloud import test as t2

def lambda_handler(event, context):
    spark = SparkSession.builder.getOrCreate()
    print('spark', spark.version)