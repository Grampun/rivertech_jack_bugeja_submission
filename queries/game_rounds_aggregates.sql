-- materialized view for hourly aggregations
-- we will be aggregating the game_round amounts by hour in this case
CREATE MATERIALIZED VIEW RIVER_TECH.hourly_aggregates
ENGINE = AggregatingMergeTree()
ORDER BY (user_id, game_id)
AS
SELECT
    toStartOfHour(created_timestamp) AS hour,
    user_id,
    game_id,
    sum(real_amount_bet) AS total_real_amount_bet,
    sum(bonus_amount_bet) AS total_bonus_amount_bet,
    sum(real_amount_win) AS total_real_amount_win,
    sum(bonus_amount_win) AS total_bonus_amount_win
FROM RIVER_TECH.game_rounds
GROUP BY hour, user_id, game_id;
