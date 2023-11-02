def solution():
    """Jeremy buys 30 watermelons. He eats 3 watermelons per week. Each week he gives 2 to his dad. How many weeks will the watermelons last?"""
    total_watermelons = 30
    watermelons_per_week = 3 + 2
    weeks_lasts = total_watermelons // watermelons_per_week
    result = weeks_lasts
    return result

print(solution())