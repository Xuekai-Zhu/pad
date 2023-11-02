def solution():
    airflow_per_second = 10  # liters
    airflow_per_minute = airflow_per_second * 60  # liters
    airflow_per_day = airflow_per_minute * 10  # liters
    airflow_per_week = airflow_per_day * 7  # liters
    result = airflow_per_week
    return result

print(solution())