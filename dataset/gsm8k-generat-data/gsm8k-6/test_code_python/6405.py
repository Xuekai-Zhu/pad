def solution():
    # Calculate the total swimming time
    total_swimming_time = 3 * 60  # Tobias was at the pool for 3 hours

    # Calculate the number of 5-minute pauses Tobias took
    num_pauses = total_swimming_time // 25

    # Calculate the total time Tobias spent swimming
    total_swimming_time -= num_pauses * 5

    # Calculate the distance Tobias swam
    distance_swam = (total_swimming_time // 5) * 100

    result = distance_swam
    return result

print(solution())