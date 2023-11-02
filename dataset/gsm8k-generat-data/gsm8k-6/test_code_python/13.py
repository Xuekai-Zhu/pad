def solution():
    # Calculate the cost of each ingredient
    cheddar_cheese_cost = 10                        # 2 pounds of cheddar cheese for $10
    cream_cheese_cost = 0.5 * cheddar_cheese_cost   # pound of cream cheese that cost half the price of the cheddar cheese
    cold_cuts_cost = 2 * cheddar_cheese_cost        # pack of cold cuts that cost twice the price of the cheddar cheese
    
    # Calculate the total cost of the ingredients
    total_cost = cheddar_cheese_cost + cream_cheese_cost + cold_cuts_cost
    result = total_cost
    return result

print(solution())