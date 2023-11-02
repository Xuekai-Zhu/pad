def solution():
    """Roberto and Valerie are jumping rope at recess. Roberto can skip 4,200 times an hour. Valerie can skip 80 times a minute. If they jump rope for fifteen minutes straight, how many skips will they total?"""
    # Calculate the number of skips Roberto can do in 15 minutes
    roberto_skips = 4200 / 4 * 15

    # Calculate the number of skips Valerie can do in 15 minutes
    valerie_skips = 80 * 15

    # Calculate the total number of skips
    total_skips = roberto_skips + valerie_skips

    result = total_skips
    return result

print(solution())