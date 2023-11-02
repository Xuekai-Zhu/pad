def solution():
    
    candy_bars_cost = 0.75 * 2
    lollipops_cost = 0.25 * 4
    total_spent = candy_bars_cost + lollipops_cost
    snow_money = total_spent * 6
    driveways = int(snow_money / 1.5)
    result = driveways
    return result

print(solution())