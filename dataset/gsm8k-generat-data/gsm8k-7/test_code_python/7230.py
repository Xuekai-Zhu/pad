def solution():
    flour_cups = 3
    sugar_cups = 2
    scoop_size = 1/3

    # Calculate the total number of flour scoops needed
    flour_scoops = flour_cups / scoop_size

    # Calculate the total number of sugar scoops needed
    sugar_scoops = sugar_cups / scoop_size

    # Calculate the total number of scoops needed
    total_scoops = flour_scoops + sugar_scoops
    result = total_scoops
    return result

print(solution())