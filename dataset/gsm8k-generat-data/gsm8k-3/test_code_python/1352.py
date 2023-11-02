def solution():
    """A fan can create an airflow of 10 liters per second. If the fan works for 10 minutes each day, calculate the amount of airflow it will create in one week."""
    # Define the airflow rate in liters per minute
    AIRFLOW_RATE = 10 * 60

    # Define the number of minutes the fan works each day
    MINUTES_PER_DAY = 10

    # Calculate the total airflow in liters for one week
    total_airflow = AIRFLOW_RATE * MINUTES_PER_DAY * 7

    # Display the total airflow for one week
    result = total_airflow
    return result

print(solution())