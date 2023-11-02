def solution():
    """Farmer Red has three milk cows: Bess, Brownie, and Daisy. Bess, the smallest cow, gives him two pails of milk every day. Brownie, the largest cow, produces three times that amount. Then Daisy makes one pail more than Bess. How many pails of milk does Farmer Red get from them each week?"""
    bess_milk = 2
    brownie_milk = 3 * bess_milk
    daisy_milk = bess_milk + 1
    total_milk_per_day = bess_milk + brownie_milk + daisy_milk
    total_milk_per_week = total_milk_per_day * 7
    result = total_milk_per_week
    return result

print(solution())