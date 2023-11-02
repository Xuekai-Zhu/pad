def solution():
    """Maryann can pick the lock on a cheap pair of handcuffs in 6 minutes and on an expensive pair of handcuffs in 8 minutes. If Maryann needs to rescue three of her friends who have expensive handcuffs on their hands and cheap handcuffs on their ankles, how long will it take for her to free all of them?"""
    # Define the time it takes Maryann to pick each type of handcuff
    cheap_time = 6
    expensive_time = 8

    # Define the number of friends who need to be rescued
    num_friends = 3

    # Calculate the total time it will take to rescue all friends
    total_time = cheap_time + expensive_time + (2 * expensive_time)

    # Adjust for the fact that all handcuffs must be picked at the same time
    total_time /= num_friends

    # Return the result
    result = total_time
    return result

print(solution())