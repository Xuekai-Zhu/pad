def solution():
    # Calculate profit per month from making cars
    car_profit = (4 * 50) - 100
    
    # Calculate profit per month from making motorcycles
    motorcycle_profit = (8 * 50) - 250
    
    # Calculate the difference in profit between making cars and motorcycles
    profit_difference = motorcycle_profit - car_profit
    
    result = profit_difference
    return result

print(solution())