def solution():
    """Kevin has a shoebox filled with toads. Every day, Kevin feeds each toad 3 worms. It takes Kevin 15 minutes to find each worm. If it takes Kevin 6 hours to find enough worms to feed all of his toads, how many toads does Kevin have in his shoebox?"""
    worms_per_toad = 3
    time_per_worm = 15
    total_worms = (6*60)//time_per_worm  # converting 6 hours to minutes
    total_toads = total_worms // worms_per_toad
    result = total_toads
    return result

print(solution())