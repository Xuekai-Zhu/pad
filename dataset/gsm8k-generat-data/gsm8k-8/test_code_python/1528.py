def solution():
    # Define the cost and the amount of money Gabby has
    cost = 65
    money_saved = 35
    
    # Add the additional money from Gabby's mom
    money_saved += 20
    
    # Calculate how much more Gabby needs to save
    money_needed = cost - money_saved
    result = money_needed
    return result

print(solution())