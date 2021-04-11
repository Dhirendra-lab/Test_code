
################################################

from pyspark.sql.functions import spark_partition_id

from pyspark.sql import SparkSession
spark=SparkSession.builder\
        .master('local')\
        .appName('Dhiren')\
        .getOrCreate()
        
sc=spark.sparkContext


from datetime import datetime

start_time=datetime.now()

df=spark.read.csv('SalesRecords.csv',header=True).cache()

df=df.filter("`Sales Channel`='Online'")

df=df.sort('Order Date')

print(df.count())

end_time=datetime.now()
print(' Duration :{}'.format(end_time-start_time))


df.explain()

df.rdd.getNumPartitions()

df.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().show()

##################################################



from pyspark.sql.functions import spark_partition_id

from pyspark.sql import SparkSession
spark=SparkSession.builder\
        .master('local')\
        .appName('Dhiren')\
        .getOrCreate()
        
sc=spark.sparkContext

from datetime import datetime

start_time=datetime.now()
df=spark.read.csv('SalesRecords.csv',header=True).cache()

df=df.sort('Order Date')

df=df.filter("`Sales Channel`='Online'")

print(df.count())
end_time=datetime.now()
print(' Duration :{}'.format(end_time-start_time))


df.explain()

df.rdd.getNumPartitions()

df.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().show()

#########################################################################



from pyspark.sql import SparkSession
from pyspark.sql.functions import spark_partition_id
spark=SparkSession.builder\
        .master('local')\
        .appName('Dhiren')\
        .getOrCreate()
        
sc=spark.sparkContext


from datetime import datetime

start_time=datetime.now()

df=spark.read.csv('SalesRecords.csv',header=True)

df=df.filter("`Sales Channel`='Online'")

df=df.sort('Order Date')

print(df.count())

end_time=datetime.now()

print(' Duration :{}'.format(end_time-start_time))


df.explain()

df.rdd.getNumPartitions()

df.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().show()


#####################################################################


from pyspark.sql.functions import spark_partition_id
from pyspark.sql import SparkSession
spark=SparkSession.builder\
        .master('local')\
        .appName('Dhiren')\
        .getOrCreate()
        
sc=spark.sparkContext


from datetime import datetime

start_time=datetime.now()
df=spark.read.csv('SalesRecords.csv',header=True)

df=df.sort('Order Date')

df=df.filter("`Sales Channel`='Online'")

print(df.count())
end_time=datetime.now()
print(' Duration :{}'.format(end_time-start_time))


df.explain()

df.rdd.getNumPartitions()

df.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().show()

























