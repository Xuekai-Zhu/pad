def solution():
    """During April, the baker sold 453 cakes at $12 and 126 pies at $7. How much did the baker earn?"""
    # Define the price of a cake and a pie
    CAKE_PRICE = 12
    PIE_PRICE = 7
    
    # Define the number of cakes and pies sold
    num_cakes = 453
    num_pies = 126
    
    # Calculate the total earnings
    total_earnings = (num_cakes * CAKE_PRICE) + (num_pies * PIE_PRICE)
    
    # Display the total earnings
    result = total_earnings
    return result

print(solution())