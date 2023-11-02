def solution():
    """A gumball machine has red, green, and blue gumballs. The machine has half as many blue gumballs as red gumballs. For each blue gumball, the machine has 4 times as many green gumballs. If the machine has 16 red gumballs how many gumballs are in the machine?"""
    # Define the number of red gumballs and calculate the number of blue gumballs and green gumballs
    red_gumballs = 16
    blue_gumballs = red_gumballs // 2
    green_gumballs = blue_gumballs * 4

    # Calculate the total number of gumballs in the machine
    total_gumballs = red_gumballs + blue_gumballs + green_gumballs

    # return the result
    result = total_gumballs
    return result

print(solution())