def solution():
    """Hannah is buying some apples for $5 per kilogram. If she would get a 40% discount on each kilogram of apples, how much would she pay for 10 kilograms of them?"""
    # Define the initial price of one kilogram of apples and the discount rate
    INITIAL_PRICE = 5
    DISCOUNT_RATE = 0.4
    
    # Calculate the discounted price per kilogram of apples
    discounted_price = INITIAL_PRICE * (1 - DISCOUNT_RATE)
    
    # Calculate the total price for 10 kilograms of apples
    total_price = discounted_price * 10
    
    result = total_price
    return result

print(solution())