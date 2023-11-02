def solution():
    """Jeremy buys 30 watermelons. He eats 3 watermelons per week. Each week he gives 2 to his dad. How many weeks will the watermelons last?"""
    total_watermelons = 30
    per_week_consumption = 3 + 2  # Jeremy eats 3 melons and gives 2 to his dad
    weeks = total_watermelons // per_week_consumption
    result = weeks
    return result

print(solution())