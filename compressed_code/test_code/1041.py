def solution():
    
    airflow_per_sec = 10
    airflow_per_min = airflow_per_sec * 60
    airflow_per_day = airflow_per_min * 10
    airflow_per_week = airflow_per_day * 7

    result = airflow_per_week
    return result

print(solution())