def solution():
    # Calculate the amount spent on bread and candy bar
    spent_on_bread = 3
    spent_on_candy = 2
    total_spent = spent_on_bread + spent_on_candy

    # Calculate the amount left to spend on Turkey
    left_to_spend = 32 - total_spent
    spent_on_turkey = left_to_spend / 3

    # Calculate the amount of money left after the purchases
    money_left = 32 - spent_on_bread - spent_on_candy - spent_on_turkey
    result = money_left
    return result

print(solution())