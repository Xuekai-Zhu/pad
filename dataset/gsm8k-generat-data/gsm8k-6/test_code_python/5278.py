def solution():
    # Calculate the number of water bottles and apple bottles in the box
    water_bottles = 2 * 12  # 2 dozen water bottles
    apple_bottles = water_bottles + 6  # half a dozen more apple bottles than water bottles
    total_bottles = water_bottles + apple_bottles  # total number of bottles
    result = total_bottles
    return result

print(solution())