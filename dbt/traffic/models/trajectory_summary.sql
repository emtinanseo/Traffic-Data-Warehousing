WITH trajectory_summary AS (
    SELECT
        track_id,
        MAX(speed) AS max_speed,
        MAX(lat_acc) AS max_lat_acc,
        MAX(lon_acc) AS max_lon_acc,
        MAX(time) AS total_time 
    FROM trajectories
    GROUP BY track_id
)

SELECT * FROM trajectory_summary