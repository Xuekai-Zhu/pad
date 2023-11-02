def solution():
    # Calculate profit for making cars
    car_material_cost = 100  # Cost of materials for making a car
    cars_produced = 4  # Number of cars produced per month
    car_sales_price = 50  # Sale price of a car
    car_profit = (car_sales_price * cars_produced) - car_material_cost

    # Calculate profit for making motorcycles
    motorcycle_material_cost = 250  # Cost of materials for making a motorcycle
    motorcycles_produced = 8  # Number of motorcycles produced per month
    motorcycle_sales_price = 50  # Sale price of a motorcycle
    motorcycle_profit = (motorcycle_sales_price * motorcycles_produced) - motorcycle_material_cost

    # Calculate the difference in profit between making cars and motorcycles
    profit_difference = motorcycle_profit - car_profit
    result = profit_difference
    return result

print(solution())