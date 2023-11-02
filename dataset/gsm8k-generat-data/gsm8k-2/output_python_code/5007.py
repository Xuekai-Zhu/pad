def solution():
    """A gumball machine has red, green, and blue gumballs. The machine has half as many blue gumballs as red gumballs. For each blue gumball, the machine has 4 times as many green gumballs. If the machine has 16 red gumballs how many gumballs are in the machine?"""
    red_gumballs = 16
    blue_gumballs = red_gumballs / 2
    green_gumballs = blue_gumballs * 4
    total_gumballs = red_gumballs + blue_gumballs + green_gumballs
    result = total_gumballs
    return result

print(solution())