def solution():
    # Calculate the total volume of liquid in ounces
    total_volume_oz = 6 * 12 + 28 + 40

    # Convert the total volume to number of 10 oz servings
    servings = total_volume_oz / 10
    result = servings
    return result

print(solution())