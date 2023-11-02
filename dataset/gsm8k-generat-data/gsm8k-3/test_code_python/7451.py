def solution():
    """A factory decides to stop making cars and start making motorcycles instead. When it made cars, per month, it cost $100 for materials, they could make 4 cars, and they sold each car for $50. Now that they make motorcycles it costs $250 for materials, but they sell 8 of them for $50 each. How much more profit do they make per month selling motorcycles instead of cars?"""
    # Define the cost and revenue for making cars
    car_material_cost = 100
    car_production_cost = car_material_cost + (50 * 4)
    car_revenue = 50 * 4

    # Define the cost and revenue for making motorcycles
    motorcycle_material_cost = 250
    motorcycle_production_cost = motorcycle_material_cost + (50 * 8)
    motorcycle_revenue = 50 * 8

    # Calculate the profit for making cars and motorcycles
    car_profit = car_revenue - car_production_cost
    motorcycle_profit = motorcycle_revenue - motorcycle_production_cost

    # Calculate the difference in profit between making motorcycles and cars
    profit_difference = motorcycle_profit - car_profit

    result = profit_difference
    return result

print(solution())