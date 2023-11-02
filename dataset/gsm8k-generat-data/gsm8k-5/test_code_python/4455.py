def solution():
    money_left_after_food = 0.4  # Abigail spent 60% on food, so she has 40% of her money left
    money_left_after_phone = 0.75 * money_left_after_food  # She spent 25% of what was left after food on her phone bill
    money_left_after_entertainment = money_left_after_phone - 20  # She spent $20 on entertainment before having $40 left

    # Calculate the initial amount of money Abigail had
    initial_money = money_left_after_entertainment / 0.05
    result = initial_money
    return result

print(solution())