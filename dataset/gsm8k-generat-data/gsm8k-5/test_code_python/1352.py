def solution():
    airflow_per_sec = 10  # The fan creates an airflow of 10 liters per second
    airflow_per_min = airflow_per_sec * 60  # convert airflow per second to airflow per minute
    airflow_per_day = airflow_per_min * 10  # The fan works for 10 minutes each day
    airflow_per_week = airflow_per_day * 7  # calculate the amount of airflow it will create in one week

    result = airflow_per_week
    return result

print(solution())