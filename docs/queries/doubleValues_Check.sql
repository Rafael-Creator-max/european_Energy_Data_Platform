/*CHECK FOR DOUBLES VALUES*/
SELECT 
    measure_item
    ,date_utc
    ,country_code
    ,COUNT(*) AS ocurrences
FROM raw.entsoe_hourly_load
GROUP BY
    measure_item
    ,date_utc
    ,country_code
HAVING COUNT(*) > 1;