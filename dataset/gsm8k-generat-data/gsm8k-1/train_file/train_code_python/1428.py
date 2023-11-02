def solution():
    """Ronald wants to make profits by re-selling some phones he bought a week ago. He bought 200 units for just $3000, and he wants to gain a third of the initial investment in profits when all units are sold. Including the profit margin, what will be the selling price for each phone?"""
    units_bought = 200
    initial_cost = 3000
    profit_percent = 33.33
    total_profit = initial_cost * (profit_percent / 100)
    total_cost = initial_cost + total_profit
    cost_per_unit = total_cost / units_bought
    result = cost_per_unit
    return result+cost_per_unit
  
# Since the question asks for the selling price, the equation has been modified to add the cost per unit to the final result.

print(solution())