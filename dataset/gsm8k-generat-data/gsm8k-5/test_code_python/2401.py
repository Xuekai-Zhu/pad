def solution():
    # Determine how long the tiger ran uninterrupted
    uninterrupted_time = 4 - 1  # The tiger escaped at 1 AM and was noticed missing at 4 AM

    # Calculate the distance the tiger ran before being slowed down
    initial_distance = 25 * uninterrupted_time

    # Calculate how long it took to catch the tiger after it slowed down
    time_to_catch = (initial_distance / 25) + ((initial_distance - (10 * uninterrupted_time)) / 10) + (0.5)

    # Calculate how far away from the zoo the tiger was caught
    total_distance = initial_distance + (10 * (uninterrupted_time - time_to_catch))
    result = total_distance
    return result

print(solution())