def solution():
    """In a race, there are eight runners. The first five runners finish the race in 8 hours, while the rest of the runners finish the race 2 hours later. Calculate the total time the eight runners took to finish the race."""
    # Define the time taken by the first five runners
    time_first_five = 8

    # Calculate the average time taken by the first five runners
    avg_time_first_five = time_first_five / 5

    # Calculate the total time taken by the last three runners
    time_last_three = (avg_time_first_five + 2) * 3

    # Calculate the total time taken by all eight runners
    total_time = time_first_five + time_last_three

    result = total_time
    return result

print(solution())