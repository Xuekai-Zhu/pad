def solution():
    starting_money = 480

    # Calculate how much money Ali spent on food
    food_cost = starting_money / 2

    # Calculate how much money Ali had left after buying food
    money_after_food = starting_money - food_cost

    # Calculate how much Ali spent on glasses
    glasses_cost = money_after_food / 3

    # Calculate how much money Ali had left after buying glasses
    money_left = money_after_food - glasses_cost
    result = money_left
    return result

print(solution())