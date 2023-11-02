def solution():
    """Ben wants to pick 56 sugar snap peas. At his current rate of picking, all will be picked in seven minutes. How long, in minutes, would it take Ben to pick 72 sugar snap peas?"""
    peas_per_minute = 56 / 7
    time_to_pick_72_peas = 72 / peas_per_minute
    result = time_to_pick_72_peas
    return result

print(solution())