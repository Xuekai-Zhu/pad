def solution():
    """Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?"""
    pills_per_day = 9
    days = 14
    cheaper_pills = pills_per_day - 4
    cost_of_cheaper_pills = 1.5 + 5.5
    total_cost_of_cheaper_pills = cheaper_pills * cost_of_cheaper_pills
    total_cost_of_expensive_pills = 4 * 7 * (1.5 + 5.5)
    total_cost = total_cost_of_cheaper_pills + total_cost_of_expensive_pills
    result = total_cost * days
    return result

print(solution())