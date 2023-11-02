def solution():
    # Calculate the amount of milk produced by each cow daily
    bess_milk = 2
    brownie_milk = 3 * bess_milk
    daisy_milk = bess_milk + 1

    # Calculate the total amount of milk produced by all cows in a week
    total_milk = (bess_milk + brownie_milk + daisy_milk) * 7

    result = total_milk
    return result

print(solution())