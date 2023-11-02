def solution():
    """James buys 20 pounds of beef and half that much pork. He uses 1.5 pounds of meat to make meals at his restaurant. Each meal sells for $20. How much money did he make?"""
    
    # Define the amount of beef purchased
    beef = 20
    
    # Calculate the amount of pork purchased
    pork = beef / 2
    
    # Calculate the total amount of meat used for meals
    meat_used = beef + pork
    
    # Calculate the number of meals that can be made
    meals = meat_used / 1.5
    
    # Calculate the total revenue from selling the meals
    total_revenue = meals * 20
    
    # Return the result
    result = total_revenue
    return result

print(solution())