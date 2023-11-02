def solution():
    scarves_per_yarn = 3
    num_red_yarns = 2
    num_blue_yarns = 6
    num_yellow_yarns = 4

    # Calculate the total number of scarves for each color of yarn
    red_scarves = num_red_yarns * scarves_per_yarn
    blue_scarves = num_blue_yarns * scarves_per_yarn
    yellow_scarves = num_yellow_yarns * scarves_per_yarn

    # Calculate the total number of scarves
    total_scarves = red_scarves + blue_scarves + yellow_scarves
    result = total_scarves
    return result

print(solution())