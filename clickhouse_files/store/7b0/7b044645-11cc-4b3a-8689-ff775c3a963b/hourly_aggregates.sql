ATTACH MATERIALIZED VIEW _ UUID '5669499f-8048-4f0c-ac2c-fc14412a9dea' TO INNER UUID '0b76ef68-3e68-4e41-8810-f582413da73d'
(
    `hour` DateTime,
    `user_id` String,
    `game_id` Int64,
    `total_real_amount_bet` Float64,
    `total_bonus_amount_bet` Float64,
    `total_real_amount_win` Float64,
    `total_bonus_amount_win` Float64
)
ENGINE = AggregatingMergeTree
ORDER BY (user_id, game_id)
SETTINGS index_granularity = 8192 AS
SELECT
    toStartOfHour(created_timestamp) AS hour,
    user_id,
    game_id,
    sum(real_amount_bet) AS total_real_amount_bet,
    sum(bonus_amount_bet) AS total_bonus_amount_bet,
    sum(real_amount_win) AS total_real_amount_win,
    sum(bonus_amount_win) AS total_bonus_amount_win
FROM RIVER_TECH.game_rounds
GROUP BY
    hour,
    user_id,
    game_id
