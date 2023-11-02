def solution():
    original_price = 100
    first_depreciation = 0.25 # 25% drop
    second_depreciation = 0.20 # 20% drop

    # Calculate the value of the mower after first depreciation
    first_value = original_price * (1 - first_depreciation)

    # Calculate the value of the mower after second depreciation
    final_value = first_value * (1 - second_depreciation)
    result = final_value
    return result

print(solution())