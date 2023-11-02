def solution():
    """If 3 crows eat 30 worms in one hour, how many worms will 5 crows eat in 2 hours?"""
    crows_1 = 3
    worms_1 = 30
    crows_2 = 5
    hours_2 = 2
    worms_2 = worms_1 * ((crows_2 * hours_2) / (crows_1 * 1))
    result = worms_2
    return result

print(solution())