def solution():
    # Calculate the number of blue and green gumballs in the machine using the ratio between them and the red gumballs
    blue_gumballs = 16 / 2  # the machine has half as many blue gumballs as red gumballs
    green_gumballs = blue_gumballs * 4  # for each blue gumball, the machine has 4 times as many green gumballs

    # Calculate the total number of gumballs in the machine
    total_gumballs = 16 + blue_gumballs + green_gumballs

    result = total_gumballs
    return result

print(solution())