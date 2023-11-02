def solution():
    """A fan can create an airflow of 10 liters per second. If the fan works for 10 minutes each day, calculate the amount of airflow it will create in one week."""
    # Define the airflow rate of the fan in liters per second
    airflow_rate = 10

    # Calculate the airflow produced in 10 minutes
    airflow_10_minutes = airflow_rate * 60 * 10

    # Calculate the airflow produced in one week (7 days)
    airflow_1_week = airflow_10_minutes * 7

    # Return the result in liters per week
    result = airflow_1_week
    return result

print(solution())