def solution():
    """Calculates the total time, in minutes, the Polar Bears spent circling the island over the weekend"""
    # Define the time it takes to navigate around the island once in minutes
    TIME_PER_ROUND = 30

    # Calculate the total time spent on Saturday
    rounds_saturday = 11
    total_time_saturday = rounds_saturday * TIME_PER_ROUND

    # Calculate the total time spent on Sunday
    rounds_sunday = 15
    total_time_sunday = rounds_sunday * TIME_PER_ROUND

    # Calculate the total time spent over the weekend
    total_time_weekend = total_time_saturday + total_time_sunday

    # Display the total time spent
    result = total_time_weekend
    return result

print(solution())