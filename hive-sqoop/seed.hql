-- CREATE TEMPORARY TABLES FOR CSV FILES, STORED AS TEXTFILE
CREATE TABLE temp_generation_leonardo_santos (
    generation INT,
    date_introduced DATE
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

CREATE TABLE temp_pokemon_leonardo_santos (
    idnum int,
    name STRING,
    hp INT,
    speed INT,
    attack INT,
    special_attack INT,
    defense INT,
    special_defense INT,
    generation INT
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;


-- LOAD DATA INTO TABLES
LOAD DATA INPATH '/user/2rp-leonardos/generation.csv'
INTO TABLE temp_generation_leonardo_santos;

LOAD DATA INPATH '/user/2rp-leonardos/pokemon.csv'
INTO TABLE temp_pokemon_leonardo_santos;


-- PUT DATA FROM TEXTFILE TO ORC
INSERT INTO TABLE  generation_leonardo_santos
SELECT * FROM temp_generation_leonardo_santos;

INSERT INTO TABLE  pokemon_Leonardo_Santos
SELECT * FROM temp_pokemon_leonardo_santos;


-- DROP TEMP TABLES
DROP TABLE temp_generation_leonardo_santos;
DROP TABLE temp_pokemon_leonardo_santos

-- JOIN
SELECT P.name, G.generation
FROM pokemon_Leonardo_Santos P 
JOIN generation_Leonardo_Santos G 
ON P.generation = G.generation

-- It took 1.45s to run this join using impala
-- However, Hive took 40.54s running the same query
