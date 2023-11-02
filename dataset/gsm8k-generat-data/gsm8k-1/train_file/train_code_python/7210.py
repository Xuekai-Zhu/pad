def solution():
    """Cary is trying to strip the ivy off a tree in her yard. She strips 6 feet of ivy every day, but the ivy grows another 2 feet every night. If the tree is covered by 40 feet of ivy, how many days will it take Cary to strip all the ivy off?"""
    daily_ivy_strip = 6
    daily_ivy_growth = 2
    total_ivy = 40
    days = 0
    
    while total_ivy > 0:
        days += 1
        total_ivy -= daily_ivy_strip
        if total_ivy <= 0:
            break
        total_ivy += daily_ivy_growth
    
    result = days
    return result

print(solution())