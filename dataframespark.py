from pyspark.sql.session import SparkSession

#importa tipos de daos
from pyspark.sql.types import(BooleanType, IntegerType, IntegralType, StringType, StructType, TimestampType, ArrayType, FloatType, StructField)

import pyspark.sql.functions as F
from pyspark.sql.functions import col, lit

spark = SparkSession. builder.appName('TFD') \
    .config('spark.master', 'local') \
    .config('spark.executor.memory', '1gb') \
    .config('spark.shuffle.sql.partitions', 1)\
    .getOrCreate()

#df = spark.read.load('C:\Sparkscripts\student_mat.csv', format='csv', sep=',', inferSchema='true', header='true')
#df.printSchema()
#print('algo')

schema = StructType([StructField('school', StringType()),
                    StructField('sex', StringType()),
                    StructField('age', IntegerType()),
                    StructField('address', StringType()),
                    StructField('famsize', StringType()),
                    StructField('pstatus', StringType()),
                    StructField('medu', IntegerType()),
                    StructField('fedu', IntegerType()),
                    StructField('mjob', StringType()),
                    StructField('fjob', StringType()),                   
                    StructField('reason', StringType()), 
                    StructField('guardian', StringType()), 
                    StructField('traveltime', IntegerType()),
                    StructField('studytime', IntegerType()),                   
                    StructField('failures', IntegerType()), 
                    StructField('schoolsup', BooleanType()),
                    StructField('famsup', BooleanType()),
                    StructField('paid', BooleanType()),
                    StructField('activities', BooleanType()),
                    StructField('nursery', BooleanType()),
                    StructField('higher', BooleanType()),
                    StructField('internet', BooleanType()),
                    StructField('romantic', BooleanType()),
                    StructField('famrel', IntegerType()),
                    StructField('freetime', IntegerType()),
                    StructField('goout', IntegerType()),
                    StructField('dalc', IntegerType()),
                    StructField('walc', IntegerType()),
                    StructField('health', IntegerType()),
                    StructField('absences', IntegerType()),
                    StructField('g1', IntegerType()),
                    StructField('g2', IntegerType()),
                    StructField('g3', IntegerType()),
])

path = 'C:\scripts\student_mat.csv'

df = spark.read.format('csv') \
    .schema(schema) \
    .load(path, sep=",", header=True)

matematicaDF = df.withColumn('Subject', lit("Math")) # Cria uma coluna adicionando o subject Math nesse dataFrame

path = 'C:\scripts\student_por.csv'

df = spark.read.format('csv') \
    .schema(schema) \
    .load(path, sep=",", header=True)

portuguesDF = df.withColumn('Subject', lit("Portuguese"))

novoDF = matematicaDF.union(portuguesDF)
#novoDF = novoDF.join(dftemp)
#novoDF.show(400)
novoDF.groupby('Subject').count().show()