def solution():
    # Define the original price of one bottle
    original_price = 15.00

    # Calculate the discounted price of one bottle
    discounted_price = 0.8 * original_price

    # Calculate the final price of one bottle with coupons
    final_price = discounted_price - 6.00

    # Calculate the total cost of three bottles
    total_cost = 3 * final_price

    result = total_cost
    return result

print(solution())