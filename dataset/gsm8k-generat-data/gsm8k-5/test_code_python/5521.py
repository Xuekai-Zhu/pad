def solution():
    # Calculate the total time needed to make the bread
    total_time = (1 * 60) + 15 + (2 * 60) + 30 + 15  # Convert all times to minutes

    # Calculate the time the head baker needs to arrive at the store
    latest_arrival_time = (6 * 60) - total_time  # Convert opening time to minutes

    result = latest_arrival_time
    return result

print(solution())