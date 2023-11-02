def solution():
    # Calculate the weight of the fruit Diego has already bought
    total_weight = 3  # 1 pound each of watermelon, grapes, and oranges
    remaining_weight = 20 - total_weight  # weight of fruit Diego can still carry
    pounds_of_apples = remaining_weight // 2  # divide remaining weight by the weight of the apples
    result = pounds_of_apples
    return result

print(solution())