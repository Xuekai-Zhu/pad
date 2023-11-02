def solution():
    # Calculate the amount spent on food
    spent_on_food = 480 / 2

    # Calculate the amount left after spending on food
    left_after_food = 480 - spent_on_food

    # Calculate the amount spent on glasses
    spent_on_glasses = left_after_food / 3

    # Calculate the amount of money left
    money_left = left_after_food - spent_on_glasses

    result = money_left
    return result

print(solution())