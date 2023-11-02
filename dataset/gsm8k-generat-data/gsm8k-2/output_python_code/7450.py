def solution():
    """A factory decides to stop making cars and start making motorcycles instead. When it made cars, per month, it cost $100 for materials, they could make 4 cars, and they sold each car for $50. Now that they make motorcycles it costs $250 for materials, but they sell 8 of them for $50 each. How much more profit do they make per month selling motorcycles instead of cars?"""
    car_materials_cost = 100
    car_production = 4
    car_sale_price = 50
    motorcycle_materials_cost = 250
    motorcycle_production = 8
    motorcycle_sale_price = 50
    car_profit = (car_sale_price * car_production) - car_materials_cost
    motorcycle_profit = (motorcycle_sale_price * motorcycle_production) - motorcycle_materials_cost
    profit_difference = motorcycle_profit - car_profit
    result = profit_difference
    return result

print(solution())