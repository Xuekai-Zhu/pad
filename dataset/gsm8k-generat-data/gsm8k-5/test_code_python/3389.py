def solution():
    original_price = 50  # The RAM was $50 before the fire outbreak
    increased_price = original_price * 1.3  # The price increased by 30%
    final_price = increased_price * 0.8  # The price fell by 20% from what it has risen after two years
    result = final_price
    return result

print(solution())