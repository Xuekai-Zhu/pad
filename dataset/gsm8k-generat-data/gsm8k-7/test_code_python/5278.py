def solution():
    num_water_bottles = 2 * 12
    num_apple_bottles = (1/2) * 12 + num_water_bottles

    # Calculate the total number of bottles in the box
    total_bottles = num_water_bottles + num_apple_bottles
    result = total_bottles
    return result

print(solution())