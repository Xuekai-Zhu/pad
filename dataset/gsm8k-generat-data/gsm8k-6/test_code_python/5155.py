def solution():
    # Calculate the number of knives in the drawer
    knives = 6 + 9

    # Calculate the number of spoons in the drawer
    spoons = 2 * knives

    # Calculate the number of teaspoons in the drawer
    teaspoons = 0.5 * 6

    # Calculate the total number of cutlery pieces in the drawer
    total_cutlery = 6 + knives + spoons + teaspoons

    # Calculate the total number of cutlery pieces after adding 2 of each cutlery
    total_cutlery += 2 * 4

    result = total_cutlery
    return result

print(solution())