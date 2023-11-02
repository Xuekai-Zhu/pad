def solution():
    """If Billy sleeps 6 hours one night, then 2 more hours than that the following night, 
    and then half the previous amount the following night, and then finally triple the previous amount 
    the final night, how much did he sleep in that four day period?"""
    night_1 = 6
    night_2 = night_1 + 2
    night_3 = night_2 / 2
    night_4 = night_3 * 3
    total_hours = night_1 + night_2 + night_3 + night_4
    result = total_hours
    return result

print(solution())