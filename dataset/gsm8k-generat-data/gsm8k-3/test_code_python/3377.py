def solution():
    """Kyle goes to basketball practice every day for 2 hours. At practice he spends half of the time shooting and the rest of the time running and weight lifting. If he runs for twice the time he spends weightlifting, how much time in minutes does he spend lifting weight?"""
    # Define the total time Kyle spends at practice each day
    PRACTICE_TIME = 2 * 60  # Convert hours to minutes

    # Calculate the time spent shooting
    shooting_time = PRACTICE_TIME / 2

    # Calculate the total time spent running and weight lifting
    rw_time = PRACTICE_TIME - shooting_time

    # Calculate the time spent weight lifting
    weightlifting_time = rw_time / 3

    # Convert weightlifting_time to minutes
    weightlifting_time = int(weightlifting_time)

    # Return the time spent lifting weights in minutes
    result = weightlifting_time
    return result

print(solution())