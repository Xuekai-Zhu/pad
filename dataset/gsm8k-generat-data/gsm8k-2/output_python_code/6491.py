def solution():
    """If 3 crows eat 30 worms in one hour, how many worms will 5 crows eat in 2 hours?"""
    crows = 5
    time = 2
    ratio = crows / 3
    worms = ratio * 30 * time
    result = worms
    return result

print(solution())