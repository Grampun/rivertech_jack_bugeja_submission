-- Create a database
CREATE DATABASE RIVER_TECH;

-- Create a table to store Avro data
CREATE TABLE RIVER_TECH.game_rounds
(
    created_timestamp Timestamp,
    game_instance_id Int64,
    user_id String,
    game_id Int64,
    real_amount_bet Float64,
    bonus_amount_bet Float64,
    real_amount_win Float64,
    bonus_amount_win Float64,
    game_name String,
    provider String
) ENGINE = MergeTree()
ORDER BY created_timestamp;
