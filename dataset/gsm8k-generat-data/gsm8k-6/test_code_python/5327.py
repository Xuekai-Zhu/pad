def solution():
    # Calculate the new prices after the increase
    new_jewelry_price = 30 + 10
    new_painting_price = 100 * 1.2  # 20% increase

    # Calculate the total price for two pieces of jewelry and five paintings
    total_price = (2 * new_jewelry_price) + (5 * new_painting_price)
    result = total_price
    return result

print(solution())