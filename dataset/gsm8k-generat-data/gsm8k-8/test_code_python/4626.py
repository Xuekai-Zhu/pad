def solution():
    # Define the cost of the other houses
    other_house_cost = 320000
    
    # Calculate the cost of building the house in question
    house_cost = other_house_cost + 100000
    
    # Calculate the selling price of the other houses
    other_house_price = 320000
    
    # Calculate the selling price of the house in question
    house_price = 1.5 * other_house_price
    
    # Calculate the profit from selling the other houses
    other_profit = other_house_price - other_house_cost
    
    # Calculate the profit from selling the house in question
    house_profit = house_price - house_cost
    
    # Calculate the difference in profit
    profit_difference = house_profit - other_profit
    
    result = profit_difference
    return result

print(solution())