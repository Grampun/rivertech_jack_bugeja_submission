ATTACH TABLE _ UUID 'a4614a80-eb3b-44d6-b85e-b413f1039bb6'
(
    `created_timestamp` DateTime,
    `game_instance_id` Int64,
    `user_id` String,
    `game_id` Int64,
    `real_amount_bet` Float64,
    `bonus_amount_bet` Float64,
    `real_amount_win` Float64,
    `bonus_amount_win` Float64,
    `game_name` String,
    `provider` String
)
ENGINE = MergeTree
ORDER BY created_timestamp
SETTINGS index_granularity = 8192
