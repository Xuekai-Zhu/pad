def solution():
    # Calculate the total airflow in 10 minutes
    airflow_in_10_min = 10 * 60 * 10  # 10 liters per second, 60 seconds per minute, runs for 10 minutes
    total_airflow_in_week = airflow_in_10_min * 7  # fan runs for 10 minutes in a day, 7 days in a week

    result = total_airflow_in_week
    return result

print(solution())