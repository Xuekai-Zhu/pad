def solution():
    initial_price = 600
    discount = 0.2  # 20% discount

    # Calculate the discounted price after negotiation
    discounted_price = initial_price * (1 - discount)

    # Return the amount paid
    result = discounted_price
    return result

print(solution())