def solution():
    """Kevin has a shoebox filled with toads. Every day, Kevin feeds each toad 3 worms. It takes Kevin 15 minutes to find each worm. If it takes Kevin 6 hours to find enough worms to feed all of his toads, how many toads does Kevin have in his shoebox?"""
    worms_per_day = 3
    time_to_find_worms = 15  # in minutes
    total_worms = 6 * 60 / time_to_find_worms * worms_per_day  # 6 hours converted to minutes
    # We know each toad gets 3 worms per day, so:
    # total_worms_needed = total_toads * 3
    # Therefore:
    total_toads = total_worms / 3
    result = total_toads
    return result

print(solution())