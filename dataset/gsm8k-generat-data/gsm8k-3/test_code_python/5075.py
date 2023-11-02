def solution():
    """There's an online sale where you get $10 for every $100 that you spend. If you make a purchase of $250 before discounts, how much did you end up paying?"""
    # Define the discount amount
    DISCOUNT = 10

    # Calculate the number of times the discount applies
    discount_times = 250 // 100

    # Calculate the total discount
    total_discount = discount_times * DISCOUNT

    # Calculate the final amount paid
    final_amount = 250 - total_discount

    # Display the final amount paid
    result = final_amount
    return result

print(solution())