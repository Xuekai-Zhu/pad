def solution():
    worms_per_toad = 3  # Kevin feeds each toad 3 worms per day
    minutes_per_worm = 15  # It takes Kevin 15 minutes to find each worm
    total_worms_time = 6 * 60  # Kevin spends 6 hours (360 minutes) finding worms

    # Calculate how many toads Kevin can feed
    worms_found = total_worms_time // minutes_per_worm
    toads_fed = worms_found // worms_per_toad

    result = toads_fed
    return result

print(solution())