def solution():
    cost_of_cars = 11 * 2  # Sarah buys 2 toy cars for $11 each
    cost_of_scarf = 10  # Sarah buys a scarf for $10 for her mother
    cost_of_beanie = 14  # Sarah buys a beanie for $14 for her brother
    remaining_money = 7  # Sarah has $7 remaining after purchasing the beanie

    # Calculate the total cost of the presents
    total_cost = cost_of_cars + cost_of_scarf + cost_of_beanie + remaining_money

    # Calculate the amount of money Sarah started with
    starting_money = total_cost + 7  # Sarah had $7 remaining after purchasing the presents
    result = starting_money
    return result

print(solution())