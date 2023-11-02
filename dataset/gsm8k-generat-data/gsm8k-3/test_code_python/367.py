def solution():
    """In a race, there are eight runners. The first five runners finish the race in 8 hours, while the rest of the runners finish the race 2 hours later. Calculate the total time the eight runners took to finish the race."""
    # Calculate the time taken by the first five runners
    first_five_time = 8

    # Calculate the total time taken by the last three runners
    last_three_time = first_five_time + 2

    # Calculate the total time taken by all eight runners
    total_time = (first_five_time * 5) + (last_three_time * 3)

    # Display the total time taken
    result = total_time
    return result

print(solution())