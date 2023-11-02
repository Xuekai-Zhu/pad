def solution():
    
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