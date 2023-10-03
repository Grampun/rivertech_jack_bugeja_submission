ATTACH TABLE _ UUID '0b76ef68-3e68-4e41-8810-f582413da73d'
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
SETTINGS index_granularity = 8192
