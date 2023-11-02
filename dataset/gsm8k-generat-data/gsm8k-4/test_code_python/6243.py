def solution():
    """Jebb buys $50 worth of food at a restaurant with a service fee of 12%. After paying, he gives a $5 tip. How much money did he spend at the restaurant?"""
    # Define the initial cost of the food
    initial_cost = 50
    
    # Calculate the service fee
    service_fee = initial_cost * 0.12
    
    # Calculate the total cost including service fee
    total_cost = initial_cost + service_fee
    
    # Add the tip
    total_cost += 5
    
    # Return the total cost
    result = total_cost
    return result

print(solution())