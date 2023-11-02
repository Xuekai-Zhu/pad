def solution():
    # Define the number of red gumballs
    red_gumballs = 16

    # Calculate the number of blue gumballs
    blue_gumballs = red_gumballs / 2

    # Calculate the number of green gumballs for each blue gumball
    green_gumballs_per_blue = 4

    # Calculate the total number of green gumballs
    green_gumballs = blue_gumballs * green_gumballs_per_blue

    # Calculate the total number of gumballs
    total_gumballs = red_gumballs + blue_gumballs + green_gumballs

    result = total_gumballs
    return result

print(solution())