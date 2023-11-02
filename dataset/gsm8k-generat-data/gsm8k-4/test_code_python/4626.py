def solution():
    """The cost of building a certain house in an area is 100,000 more than the construction cost of each of the houses in the area.  But it sells for 1.5 times as much as the other houses, which sell at $320,000 each. How much more profit is made by spending the extra money to build?"""
    # Define the construction cost of each house in the area
    construction_cost = 320000
    
    # Define the cost of building the certain house
    certain_house_cost = construction_cost + 100000
    
    # Calculate the selling price of each house in the area
    selling_price = 1.5 * construction_cost
    
    # Calculate the profit per house in the area
    profit_per_house = selling_price - construction_cost
    
    # Calculate the profit per certain house
    certain_house_profit = 1.5 * certain_house_cost - certain_house_cost
    
    # Calculate the difference in profit
    profit_difference = certain_house_profit - profit_per_house
    
    # Return the result
    result = profit_difference
    return result

print(solution())