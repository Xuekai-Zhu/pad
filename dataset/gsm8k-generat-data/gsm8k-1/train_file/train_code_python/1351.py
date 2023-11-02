def solution():
    """A fan can create an airflow of 10 liters per second. If the fan works for 10 minutes each day, calculate the amount of airflow it will create in one week."""
    airflow_per_second = 10
    seconds_per_minute = 60
    minutes_per_day = 10
    days_per_week = 7
    total_seconds = seconds_per_minute * minutes_per_day * days_per_week
    total_airflow = total_seconds * airflow_per_second
    result = total_airflow
    return result

print(solution())