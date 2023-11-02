def solution():
    """Charlotte needs to know how much money to have with her when she goes to the shoe store. How much money should Charlotte bring to buy a pair of boots, if the original price is $90 and there is a discount of 20%?"""
    # Define the original price and discount percentage
    original_price = 90
    discount_percent = 0.2

    # Calculate the discount amount
    discount_amount = original_price * discount_percent

    # Calculate the sale price
    sale_price = original_price - discount_amount

    # Display the sale price
    result = sale_price
    return result

print(solution())