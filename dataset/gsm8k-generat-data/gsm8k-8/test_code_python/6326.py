def solution():
    # Calculate how much money Ali spent on food
    food_cost = 480/2

    # Calculate how much money Ali had left after buying food
    remaining_money = 480 - food_cost

    # Calculate how much money Ali spent on glasses
    glasses_cost = remaining_money / 3

    # Calculate how much money Ali had left after buying glasses
    money_left = remaining_money - glasses_cost
    result = money_left
    return result

print(solution())