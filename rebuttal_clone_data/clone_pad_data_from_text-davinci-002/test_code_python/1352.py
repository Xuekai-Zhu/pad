def solution():
    airflow_rate = 10
    minutes_per_day = 10
    seconds_per_minute = 60
    seconds_per_day = minutes_per_day * seconds_per_minute
    seconds_per_week = days_per_week * seconds_per_day
    total_airflow = airflow_rate * seconds_per_week
    result = total_airflow
    return result

print(solution())