def solution():
    apple_price = 5  # $5 per kilogram
    discount = 0.4  # 40% discount
    num_kilograms = 10

    # Calculate the discounted price per kilogram
    discounted_price = apple_price - (apple_price * discount)

    # Calculate the total cost of all apples
    total_cost = discounted_price * num_kilograms
    result = total_cost
    return result

print(solution())