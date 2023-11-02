def solution():
    worms_per_toad = 3
    time_per_worm = 15  # in minutes
    total_time = 6 * 60  # in minutes

    # Calculate the number of worms Kevin finds in total
    total_worms = total_time / time_per_worm

    # Calculate the number of toads Kevin has
    num_toads = total_worms / worms_per_toad
    result = num_toads
    return result

print(solution())