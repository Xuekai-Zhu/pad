def solution():
    
    bess_daily_milk = 2
    brownie_daily_milk = bess_daily_milk * 3
    daisy_daily_milk = bess_daily_milk + 1
    total_daily_milk = bess_daily_milk + brownie_daily_milk + daisy_daily_milk
    total_weekly_milk = total_daily_milk * 7
    result = total_weekly_milk
    return result

print(solution())