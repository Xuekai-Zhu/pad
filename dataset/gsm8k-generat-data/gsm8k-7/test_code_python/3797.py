def solution():
    starting_money = 10
    cupcakes_cost = starting_money / 5
    remaining_money = 3

    # Calculate the amount spent on the milkshake
    milkshake_cost = starting_money - cupcakes_cost - remaining_money
    result = milkshake_cost
    return result

print(solution())