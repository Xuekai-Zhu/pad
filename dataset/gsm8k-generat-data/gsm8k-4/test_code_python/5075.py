def solution():
    """There's an online sale where you get $10 for every $100 that you spend. If you make a purchase of $250 before discounts, how much did you end up paying?"""
    # Define the purchase price before discount
    purchase_price = 250

    # Calculate the discount amount
    discount_amount = (purchase_price // 100) * 10

    # Calculate the final purchase price after discount
    final_price = purchase_price - discount_amount

    # Return the final purchase price
    result = final_price
    return result

print(solution())