def solution():
    bess_milk = 2
    brownie_milk = bess_milk * 3
    daisy_milk = bess_milk + 1

    # Calculate the total amount of milk produced by all cows in one day
    total_milk_per_day = bess_milk + brownie_milk + daisy_milk

    # Calculate the total amount of milk produced by all cows in one week (7 days)
    total_milk_per_week = total_milk_per_day * 7
    result = total_milk_per_week
    return result

print(solution())