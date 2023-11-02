def solution():
    price_for_6_apples = 3
    price_for_10_apples = 4
    savings_for_10_apples = price_for_6_apples - price_for_10_apples
    savings_per_apple = savings_for_10_apples / 10
    result = savings_per_apple * 100
    return result

print(solution())