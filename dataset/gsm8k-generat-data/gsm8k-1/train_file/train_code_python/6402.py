def solution():
    """An archer needs to practice. He intends to shoot 200 shots 4 days a week. He is able to recover 20% of his arrows. The arrows he uses cost $5.5 per arrow. His team agrees to pay for 70% of the cost of his arrows. How much does he spend for arrows a week?"""
    shots_per_day = 200
    days_per_week = 4
    arrows_per_week = (shots_per_day * days_per_week) * (1 - 0.2)
    arrow_cost = 5.5
    team_coverage = 0.7
    total_arrow_cost = arrows_per_week * arrow_cost
    archer_cost = total_arrow_cost * (1 - team_coverage)
    result = archer_cost
    return result

print(solution())