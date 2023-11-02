def solution():
    """Cary is trying to strip the ivy off a tree in her yard. She strips 6 feet of ivy every day, but the ivy grows another 2 feet every night. If the tree is covered by 40 feet of ivy, how many days will it take Cary to strip all the ivy off?"""
    ivy_length = 40
    strip_per_day = 6
    regrow_per_night = 2
    days = 0
    while ivy_length > 0:
        ivy_length -= strip_per_day
        days += 1
        if ivy_length <= 0:
            break
        ivy_length += regrow_per_night

    result = days
    return result

print(solution())