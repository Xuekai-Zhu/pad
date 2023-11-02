def solution():
    """Hannah is buying some apples for $5 per kilogram. If she would get a 40% discount on each kilogram of apples, how much would she pay for 10 kilograms of them?"""
    # Define the price per kilogram and the discount percentage
    PRICE_PER_KG = 5
    DISCOUNT_PERCENT = 40

    # Calculate the discounted price per kilogram
    discounted_price = PRICE_PER_KG - (PRICE_PER_KG * DISCOUNT_PERCENT / 100)

    # Calculate the total cost for 10 kilograms of apples
    total_cost = 10 * discounted_price

    # Display the total cost
    result = total_cost
    return result

print(solution())