def solution():
    # Calculate the total area of the wall that needs to be covered for two coats
    total_area = 600 * 2

    # Calculate the number of gallons of paint needed
    gallons_needed = total_area / 400

    # Round up to the nearest whole number of cans
    cans_needed = math.ceil(gallons_needed)

    result = cans_needed
    return result

print(solution())