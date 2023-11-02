def solution():
    """I bought a pair of shoes for $51. The shoes were already marked 75% off. What is the original price of the shoes?"""
    # Define the final price and the discount percentage
    final_price = 51
    discount_percentage = 75

    # Calculate the original price using the formula: original price = final price / (1 - discount percentage/100)
    original_price = final_price / (1 - discount_percentage/100)

    # return the result
    result = original_price
    return result

print(solution())