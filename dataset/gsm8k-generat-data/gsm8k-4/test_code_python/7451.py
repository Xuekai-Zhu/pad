def solution():
    """A factory decides to stop making cars and start making motorcycles instead. When it made cars, per month, it cost $100 for materials, they could make 4 cars, and they sold each car for $50. Now that they make motorcycles it costs $250 for materials, but they sell 8 of them for $50 each. How much more profit do they make per month selling motorcycles instead of cars?"""
    # Calculate the cost per car and the revenue per car
    car_cost = 100
    car_revenue = 50
    car_profit = car_revenue - car_cost

    # Calculate the cost per motorcycle and the revenue per motorcycle
    motorcycle_cost = 250
    motorcycle_revenue = 8 * 50
    motorcycle_profit = motorcycle_revenue - motorcycle_cost

    # Calculate the difference in profit between making cars and making motorcycles
    profit_difference = motorcycle_profit - (4 * car_profit)

    result = profit_difference
    return result

print(solution())