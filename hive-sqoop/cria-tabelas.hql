CREATE TABLE generation_Leonardo_Santos (
    generation INT,
    date_introduced DATE
    ) STORED AS ORC;

CREATE TABLE pokemon_Leonardo_Santos (
    idnum int,
    name STRING,
    hp INT,
    speed INT,
    attack INT,
    special_attack INT,
    defense INT,
    special_defense INT,
    generation INT
    ) STORED AS ORC;
