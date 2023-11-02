def solution():
    initial_money = 480  # Ali has $480 at the beginning
    food_expenses = initial_money / 2  # Ali spends half of his money on food
    remaining_money = initial_money - food_expenses  # Ali has this much money left after buying food
    glasses_expenses = remaining_money / 3  # Ali spends a third of his remaining money on glasses
    remaining_money -= glasses_expenses  # Ali has this much money left after buying glasses
    result = remaining_money
    return result

print(solution())