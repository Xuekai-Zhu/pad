def solution():
    """Farmer Red has three milk cows: Bess, Brownie, and Daisy. Bess, the smallest cow, gives him two pails of milk every day.
    Brownie, the largest cow, produces three times that amount. Then Daisy makes one pail more than Bess.
    How many pails of milk does Farmer Red get from them each week?"""
    bess_daily_milk = 2
    brownie_daily_milk = bess_daily_milk * 3
    daisy_daily_milk = bess_daily_milk + 1
    total_daily_milk = bess_daily_milk + brownie_daily_milk + daisy_daily_milk
    total_weekly_milk = total_daily_milk * 7
    result = total_weekly_milk
    return result

print(solution())