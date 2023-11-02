def solution():
    """Maryann can pick the lock on a cheap pair of handcuffs in 6 minutes and on an expensive pair of handcuffs in 8 minutes. If Maryann needs to rescue three of her friends who have expensive handcuffs on their hands and cheap handcuffs on their ankles, how long will it take for her to free all of them?"""
    # Define the time it takes to pick the lock on a cheap pair of handcuffs
    cheap_time = 6

    # Define the time it takes to pick the lock on an expensive pair of handcuffs
    expensive_time = 8

    # Define the number of handcuffs Maryann needs to unlock
    num_handcuffs = 6

    # Calculate the total time it will take for Maryann to unlock all the handcuffs
    total_time = cheap_time + expensive_time + expensive_time + expensive_time + cheap_time + cheap_time

    # Display the total time
    result = total_time
    return result

print(solution())