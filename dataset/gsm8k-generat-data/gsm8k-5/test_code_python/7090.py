def solution():
    total_berriers = 1100 #Total count of berries

    # Let the number of berries Skylar has be 'x'
    # Then Steve has '2x' berries, and Stacy has '4(2x)' berries = '8x' berries
    # Total berries = x + 2x + 8x = 11x
    # So, x = total_berriers / 11, and Stacy has 8x berries
    x = total_berriers / 11
    number_of_berriers_stacy_has = 8 * x
    result = number_of_berriers_stacy_has
    return result

print(solution())