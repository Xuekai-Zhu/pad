def solution():
    """Last week, a farmer shipped 10 boxes of pomelos which had 240 pomelos in all. This week, the farmer shipped 20 boxes. How many dozens of pomelos did the farmer ship in all?"""
    last_week_boxes = 10
    last_week_pomelos = 240
    this_week_boxes = 20
    total_pomelos = last_week_pomelos + this_week_boxes * 12
    total_dozen = total_pomelos / 12
    result = total_dozen
    return result

print(solution())