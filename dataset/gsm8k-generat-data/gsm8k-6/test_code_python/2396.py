def solution():
    # Calculate the total volume of liquid in the punch
    total_volume = 6*12 + 28 + 40  # 6 cans of 12 oz mountain dew, 28 oz of ice, and 40 oz of fruit juice

    # Calculate the number of 10 oz servings of punch
    servings = total_volume // 10  # round down to the nearest integer
    result = servings
    return result

print(solution())