def solution():
    # Calculate the total amount of soy sauce needed in ounces
    total_soy_sauce = (2 + 1 + 3) * 8

    # Calculate the number of bottles needed, rounded up to the nearest whole number
    num_bottles = math.ceil(total_soy_sauce / 16)

    result = num_bottles
    return result

print(solution())