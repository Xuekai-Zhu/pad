def solution():
    """Kyle goes to basketball practice every day for 2 hours. At practice he spends half of the time shooting and the rest of the time running and weight lifting. If he runs for twice the time he spends weightlifting, how much time in minutes does he spend lifting weight?"""
    # Define the total practice time in minutes
    total_time = 2 * 60

    # Calculate the time spent shooting
    shooting_time = total_time / 2

    # Calculate the time spent running and weight lifting
    rw_time = total_time - shooting_time

    # Let x be the time spent weight lifting, then the time spent running would be 2x
    x = rw_time / 3

    # Convert the time spent weight lifting to minutes
    weightlifting_time = x * 60

    # Return the result
    result = weightlifting_time
    return result

print(solution())