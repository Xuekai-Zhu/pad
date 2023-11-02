def solution():
    """Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?"""
    pills_per_day = 9
    days = 14
    expensive_pills = pills_per_day - 4
    expensive_price = 1.5 + 5.5
    total_expensive_cost = expensive_pills * expensive_price
    cheap_pills = 4
    cheap_price = 1.5
    total_cheap_cost = cheap_pills * cheap_price
    total_cost = (total_expensive_cost + total_cheap_cost) * days
    result = total_cost
    return result

print(solution())