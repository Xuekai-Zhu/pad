def solution():
    """If Billy sleeps 6 hours one night, then 2 more hours than that the following night, and then half the previous amount the following night, and then finally triple the previous amount the final night, how much did he sleep in that four day period?"""
    night1 = 6
    night2 = night1 + 2
    night3 = night2 / 2
    night4 = night3 * 3
    total_hours = night1 + night2 + night3 + night4
    result = total_hours
    return result

print(solution())