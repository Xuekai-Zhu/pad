def solution():
    # Define the original price of the shoes
    original_price = 125

    # Apply the 10% discount for all mothers
    discounted_price = original_price * 0.9

    # Apply the additional 4% discount for mothers with 3+ children
    if (4 >= 3):
        discounted_price = discounted_price * 0.96

    # Round the final price to 2 decimal places
    final_price = round(discounted_price, 2)
    result = final_price
    return result

print(solution())