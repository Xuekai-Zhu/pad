def solution():
    """Last week, a farmer shipped 10 boxes of pomelos which had 240 pomelos in all. This week, the farmer shipped 20 boxes. How many dozens of pomelos did the farmer ship in all?"""
    total_pomelos = 240 + (20 * (240/10)) # 240 is for last week, second part calculates total pomelos for this week
    dozens = total_pomelos / 12
    result = dozens
    return result

print(solution())