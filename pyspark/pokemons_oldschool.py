from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .getOrCreate()

pokemonDF = spark.sql("select * from work_dataeng.pokemon_leonardo_santos")
generationDF = spark.sql("select * from work_dataeng.generation_leonardo_santos")


from pyspark.sql import functions as f
generationDF.show()
genunder2002 = generationDF.where(generationDF.date_introduced < '2002-11-21').cache()
genunder2002.show()


dfJoined = pokemonDF.join(generationDF, 'generation', how='inner')
dfJoined.show(5)


dfJoined.createOrReplaceTempView("TempView")
spark.sql("""CREATE TABLE IF NOT EXISTS work_dataeng.pokemons_oldschool_leonardo_santos AS
    SELECT * FROM TempView""")
