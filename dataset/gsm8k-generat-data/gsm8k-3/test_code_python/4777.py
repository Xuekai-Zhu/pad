def solution():
    """Big Lots is having a sale. All chairs are 25% off. If you buy more than 5 chairs, you get an additional 1/3 off the discounted price of the number of chairs over 5. If you bought 8 chairs that were normally priced at $20, how much do the chairs cost in total?"""
    # Define the original price per chair
    ORIGINAL_PRICE = 20
    
    # Calculate the discounted price per chair
    discounted_price = ORIGINAL_PRICE * 0.75
    
    # Calculate the cost of the first 5 chairs
    first_five_cost = 5 * discounted_price
    
    # Calculate the cost of the remaining 3 chairs at the discounted price
    remaining_chairs_discounted = 3 * discounted_price * (2/3)
    
    # Calculate the total cost of all 8 chairs
    total_cost = first_five_cost + remaining_chairs_discounted
    
    # Display the total cost
    result = total_cost
    return result

print(solution())