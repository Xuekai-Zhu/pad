def solution():
    num_red = 16
    num_blue = num_red / 2
    num_green = num_blue * 4

    # Calculate the total number of gumballs in the machine
    total_num_gumballs = num_red + num_blue + num_green
    result = total_num_gumballs
    return result

print(solution())