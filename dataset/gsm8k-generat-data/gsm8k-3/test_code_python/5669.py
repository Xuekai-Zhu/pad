def solution():
    """Jett bought a cow from the market at $600 and took it to his farm. He spent $20 every day to buy food. He also used $500 to vaccinate and deworm the cow. If he sold the cow for $2500 after 40 days, calculate the profit he made from selling back the cow to the market."""
    
    # Define the initial cost of buying the cow
    cow_cost = 600
    
    # Calculate the cost of feeding the cow for 40 days
    food_cost = 20 * 40
    
    # Calculate the cost of vaccinating and deworming the cow
    medical_cost = 500
    
    # Calculate the total cost of owning the cow
    total_cost = cow_cost + food_cost + medical_cost
    
    # Calculate the profit from selling the cow
    selling_price = 2500
    profit = selling_price - total_cost
    
    # Display the profit
    result = profit
    return result

print(solution())