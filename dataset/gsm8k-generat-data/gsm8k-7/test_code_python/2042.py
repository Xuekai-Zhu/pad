def solution():
    saved_money = 400
    fraction_spent_on_supplies = 1/4
    fraction_spent_on_food = 1/2

    # Calculate the amount spent on school supplies
    amount_spent_on_supplies = saved_money * fraction_spent_on_supplies

    # Calculate the amount left after buying school supplies
    remaining_money = saved_money - amount_spent_on_supplies

    # Calculate the amount spent on food for the faculty
    amount_spent_on_food = remaining_money * fraction_spent_on_food

    # Calculate the amount left after spending on food
    amount_left = remaining_money - amount_spent_on_food
    result = amount_left
    return result

print(solution())