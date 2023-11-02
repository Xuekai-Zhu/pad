def solution():
    """Jon drinks a bottle of water that is 16 ounces every 4 hours for the 16 hours he is awake. Twice a day he also drinks a bottle that is 25% larger than those bottles. How much fluid does he drink a week?"""
    regular_bottle_size = 16
    extra_bottle_size = regular_bottle_size * 1.25
    regular_bottles_per_day = 16 // 4  # 4 hours per bottle
    extra_bottles_per_day = 2
    total_fluid_per_day = (regular_bottle_size * regular_bottles_per_day) + (extra_bottle_size * extra_bottles_per_day)
    total_fluid_per_week = total_fluid_per_day * 7
    result = total_fluid_per_week
    return result

print(solution())