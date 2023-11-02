def solution():
    # Calculate the area of the kitchen floor
    kitchen_area = 48 * 72

    # Calculate the number of tiles needed, rounded up to the nearest whole number
    tiles_needed = math.ceil(kitchen_area / 6)

    result = tiles_needed
    return result

print(solution())