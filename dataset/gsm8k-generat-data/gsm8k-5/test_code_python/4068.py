def solution():
    # Time it takes for Maryann to pick the cheap handcuffs
    time_cheap = 6

    # Time it takes for Maryann to pick the expensive handcuffs
    time_expensive = 8

    # Number of friends with expensive handcuffs
    num_expensive = 3

    # Number of friends with cheap handcuffs
    num_cheap = 3

    # Total time it takes for Maryann to unlock all the handcuffs
    total_time = (time_expensive * num_expensive) + (time_cheap * num_cheap)

    result = total_time
    return result

print(solution())