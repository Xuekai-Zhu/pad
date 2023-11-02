def solution():
    # Calculate the amount of money Darwin spent on gas
    gas_cost = 600 / 3

    # Calculate the amount of money Darwin had left after buying gas
    remaining_money = 600 - gas_cost

    # Calculate the amount of money Darwin spent on food
    food_cost = remaining_money / 4

    # Calculate the amount of money Darwin has left
    final_money = remaining_money - food_cost
    result = final_money
    return result

print(solution())