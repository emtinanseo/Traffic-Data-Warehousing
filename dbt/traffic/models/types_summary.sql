WITH type_summary AS (
    SELECT
        type,
        COUNT(track_id) AS count,
        AVG(traveled_d) AS avg_distance,
        AVG(avg_speed) AS avg_speed
    FROM vehicles
    GROUP BY type
)

SELECT * FROM type_summary