def solution():
    red_gumballs = 16  # Given that the machine has 16 red gumballs
    blue_gumballs = red_gumballs / 2  # Given that the machine has half as many blue gumballs as red gumballs
    green_gumballs_per_blue = 4  # Given that for each blue gumball, the machine has 4 times as many green gumballs
    green_gumballs = blue_gumballs * green_gumballs_per_blue  # Calculate the number of green gumballs
    total_gumballs = red_gumballs + blue_gumballs + green_gumballs  # Calculate the total number of gumballs
    result = total_gumballs
    return result

print(solution())