def solution():
    
    bess_milk = 2
    brownie_milk = 3 * bess_milk
    daisy_milk = bess_milk + 1
    total_milk_per_day = bess_milk + brownie_milk + daisy_milk
    total_milk_per_week = total_milk_per_day * 7
    result = total_milk_per_week
    return result

print(solution())