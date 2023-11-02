def solution():
    initial_money = 600

    # Calculate the amount spent on gas
    gas_spent = initial_money / 3

    # Calculate the remaining amount after gas was purchased
    remaining_money = initial_money - gas_spent

    # Calculate the amount spent on food
    food_spent = remaining_money / 4

    # Calculate the total amount of money Darwin has left
    total_leftover_money = remaining_money - food_spent
    result = total_leftover_money
    return result

print(solution())