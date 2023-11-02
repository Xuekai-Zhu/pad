def solution():
    discounted_price = 480
    discount = 0.2 # 20% discount

    # Calculate the original price of the shoes
    original_price = discounted_price / (1 - discount)

    result = original_price
    return result

print(solution())