def solution():
    # Define the variables
    discounted_price = 480
    discount_percent = 20

    # Calculate the original price
    original_price = discounted_price / (1 - discount_percent/100)
    result = original_price
    return result

print(solution())