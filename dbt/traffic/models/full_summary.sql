WITH full_summary AS (
    SELECT
        v.track_id,
        v.type,
        v.traveled_d AS full_distance,
        t.total_time,
        v.avg_speed,
        t.max_speed,
        t.max_lat_acc,
        t.max_lon_acc
    FROM 
        vehicles AS v
    INNER JOIN {{ ref('trajectory_summary') }} AS t 
    USING(track_id)
)

SELECT * FROM full_summary