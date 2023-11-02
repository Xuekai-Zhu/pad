def solution():
    """An archer needs to practice. He intends to shoot 200 shots 4 days a week. He is able to recover 20% of his arrows. The arrows he uses cost $5.5 per arrow. His team agrees to pay for 70% of the cost of his arrows. How much does he spend for arrows a week?"""
    num_shots_per_day = 200
    num_days = 4
    total_shots = num_shots_per_day * num_days
    num_lost_arrows = int(total_shots * 0.8)
    num_bought_arrows = total_shots - num_lost_arrows
    team_coverage = 0.7
    cost_per_arrow = 5.5
    total_spent = num_bought_arrows * cost_per_arrow * (1 - team_coverage)
    result = total_spent
    return result

print(solution())