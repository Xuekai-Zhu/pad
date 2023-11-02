def solution():
    """Bryan bought 5 t-shirts and 4 pairs of pants for $1500. If a t-shirt costs $100, how much does each pair of pants cost?"""
    
    # Define the cost of a t-shirt
    TSHIRT_COST = 100
    
    # Define the number of t-shirts and pairs of pants purchased
    num_tshirts = 5
    num_pants = 4
    
    # Calculate the total cost of the t-shirts
    tshirt_cost = num_tshirts * TSHIRT_COST
    
    # Calculate the cost of the pants
    pants_cost = 1500 - tshirt_cost
    
    # Calculate the cost of a pair of pants
    cost_per_pant = pants_cost / num_pants
    
    # Display the cost of a pair of pants
    result = cost_per_pant
    return result

print(solution())