def solution():
    # Calculate the profit from selling cars
    cars_cost = 100 * 4  # cost of materials to make 4 cars
    cars_sales = 4 * 50  # sales revenue from selling 4 cars
    cars_profit = cars_sales - cars_cost  # profit from selling 4 cars

    # Calculate the profit from selling motorcycles
    motorcycles_cost = 250  # cost of materials to make 8 motorcycles
    motorcycles_sales = 8 * 50  # sales revenue from selling 8 motorcycles
    motorcycles_profit = motorcycles_sales - motorcycles_cost  # profit from selling 8 motorcycles

    # Calculate the difference in profit between selling cars and motorcycles
    profit_difference = motorcycles_profit - cars_profit
    result = profit_difference
    return result

print(solution())