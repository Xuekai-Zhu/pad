def solution():
    # Define the amount of airflow created by the fan in one minute
    airflow_per_minute = 10 * 60

    # Calculate the total amount of airflow created by the fan in one day
    airflow_per_day = airflow_per_minute * 10

    # Calculate the total amount of airflow created by the fan in one week (7 days)
    airflow_per_week = airflow_per_day * 7
    result = airflow_per_week
    return result

print(solution())