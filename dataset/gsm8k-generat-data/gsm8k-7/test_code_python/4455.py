def solution():
    total_money_left = 40
    money_spent_on_entertainment = 20
    money_spent_on_phone_bill = 0.25 * (total_money_left - 0.75 * total_money_left)
    money_remaining_after_food_and_phone_bill = total_money_left - money_spent_on_entertainment - money_spent_on_phone_bill
    initial_money = money_remaining_after_food_and_phone_bill / 0.4
    result = initial_money
    return result

print(solution())