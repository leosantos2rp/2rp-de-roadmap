from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .getOrCreate()

pokemonDF = spark.table('work_dataeng.pokemon_leonardo_santos')
generationDF = spark.table('work_dataeng.generation_leonardo_santos')

genunder2002 = generationDF.where(generationDF.date_introduced < '2002-11-21').cache()
genunder2002.show()

dfJoined = pokemonDF.join(generationDF, 'generation', how='inner')
dfJoined.show(5)

dfJoined.write.mode('overwrite').format('orc') \
        .saveAsTable('work_dataeng.pokemons_oldschool_leonardo_santos')
