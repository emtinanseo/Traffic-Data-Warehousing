WITH distance_summary AS (
    SELECT
        full_distance,
        type,
        COUNT(track_id) as count,
        AVG(total_time) as avg_duration,
        AVG(avg_speed) as avg_speed,
        AVG(max_speed) as max_speed,
        AVG(max_lat_acc) as max_lat_acc,
        AVG(max_lon_acc) as max_lon_acc
    FROM 
        {{ ref('full_summary') }}
    GROUP BY full_distance, type
)

SELECT * FROM distance_summary