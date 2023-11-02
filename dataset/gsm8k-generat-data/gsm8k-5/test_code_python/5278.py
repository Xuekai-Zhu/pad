def solution():
    water_bottles = 2 * 12  # A box has 2 dozen water bottles
    apple_bottles = (1/2) * 12 + water_bottles  # A box has half a dozen more apple bottles than water bottles

    # Calculate the total number of bottles in the box
    total_bottles = water_bottles + apple_bottles
    result = total_bottles
    return result

print(solution())