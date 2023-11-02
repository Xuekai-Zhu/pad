def solution():
    """Maryann can pick the lock on a cheap pair of handcuffs in 6 minutes and on an expensive pair of handcuffs in 8 minutes. If Maryann needs to rescue three of her friends who have expensive handcuffs on their hands and cheap handcuffs on their ankles, how long will it take for her to free all of them?"""
    cheap_time = 6
    expensive_time = 8
    num_friends = 3
    total_time = cheap_time*2 + expensive_time*num_friends
    result = total_time
    return result

print(solution())