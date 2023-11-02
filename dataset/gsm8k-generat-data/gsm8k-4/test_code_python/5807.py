def solution():
    """Calculate the total time, in minutes, the Polar Bears spent circling the island over the weekend."""
    # Define the time it takes to fully navigate around the island
    island_time = 30

    # Calculate the time spent circling the island on Saturday
    saturday_rounds = 11
    saturday_time = saturday_rounds * island_time

    # Calculate the time spent circling the island on Sunday
    sunday_rounds = 15
    sunday_time = sunday_rounds * island_time

    # Calculate the total time spent circling the island over the weekend
    total_time = saturday_time + sunday_time

    # return the result
    result = total_time
    return result

print(solution())