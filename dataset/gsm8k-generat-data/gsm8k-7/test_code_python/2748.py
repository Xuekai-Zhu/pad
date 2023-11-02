def solution():
    original_price = 400
    discount = 0.15  # 15% decrease
    increase = 0.4  # 40% increase

    # Calculate the discounted price
    discounted_price = original_price - (original_price * discount)

    # Calculate the final price after the increase
    final_price = discounted_price + (discounted_price * increase)
    result = final_price
    return result

print(solution())