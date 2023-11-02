def solution():
    
    airflow_per_second = 10
    seconds_per_minute = 60
    minutes_per_day = 10
    days_per_week = 7
    total_seconds = seconds_per_minute * minutes_per_day * days_per_week
    total_airflow = total_seconds * airflow_per_second
    result = total_airflow
    return result

print(solution())