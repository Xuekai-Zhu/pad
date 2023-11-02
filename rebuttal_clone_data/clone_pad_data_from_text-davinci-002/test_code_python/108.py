def solution():
    """Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?"""
    pills_per_day = 9
    days = 14
    pills_1_50 = 4
    pills_5_50 = pills_per_day - pills_1_50
    cost_1_50 = 1.50
    cost_5_50 = 5.50
    total_cost = (pills_1_50 * cost_1_50) + (pills_5_50 * cost_5_50)
    result = total_cost
    return result

print(solution())