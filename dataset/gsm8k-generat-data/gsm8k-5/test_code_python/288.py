def solution():
    cheap_gym_cost = 120  # $10 per month for 12 months + $50 sign-up fee
    expensive_gym_cost = 4 * (3 * 10)  # 4 months of the expensive gym cost $120 (3 times more expensive)
    total_cost = cheap_gym_cost + expensive_gym_cost
    result = total_cost
    return result

print(solution())