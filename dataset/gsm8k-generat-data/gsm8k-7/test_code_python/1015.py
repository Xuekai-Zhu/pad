def solution():
    calories_per_orange = 80
    cost_per_orange = 1.2
    total_calories_needed = 400
    available_money = 10

    # Calculate the total number of oranges Timmy needs to buy
    num_oranges_needed = total_calories_needed / calories_per_orange

    # Calculate the cost of all the oranges Timmy needs to buy
    total_cost = num_oranges_needed * cost_per_orange

    # Calculate how much money Timmy will have left after buying the oranges he needs
    money_left = available_money - total_cost
    result = money_left
    return result

print(solution())