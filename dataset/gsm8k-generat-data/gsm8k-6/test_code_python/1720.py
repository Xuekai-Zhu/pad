def solution():
    # Calculate the original price of the shoes
    discounted_price = 480
    discount_percentage = 20
    original_price = discounted_price / (1 - (discount_percentage/100))

    result = original_price
    return result

print(solution())