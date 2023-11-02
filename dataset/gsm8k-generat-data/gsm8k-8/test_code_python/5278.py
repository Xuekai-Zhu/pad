def solution():
    # Define the number of water bottles in the box
    water_bottles = 2 * 12

    # Define the number of apple bottles in the box (half a dozen more than water bottles)
    apple_bottles = water_bottles + 6

    # Calculate the total number of bottles in the box
    total_bottles = water_bottles + apple_bottles
    result = total_bottles
    return result

print(solution())