def solution():
    """While passing by a store, Miley noticed that a bag that cost $150 last week is now on sale for $135. What percent is the discount?"""
    # Define the original price and the sale price
    original_price = 150
    sale_price = 135

    # Calculate the amount of the discount
    discount_amount = original_price - sale_price

    # Calculate the percentage of the discount
    discount_percentage = (discount_amount / original_price) * 100

    # Display the discount percentage
    result = discount_percentage
    return result

print(solution())