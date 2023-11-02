def solution():
    num_forks = 6
    num_knives = num_forks + 9
    num_spoons = num_knives * 2
    num_teaspoons = num_forks / 2
    num_added_cutlery = 2

    # Calculate the total number of each type of cutlery after 2 of each is added
    total_forks = num_forks + num_added_cutlery
    total_knives = num_knives + num_added_cutlery
    total_spoons = num_spoons + num_added_cutlery
    total_teaspoons = num_teaspoons + num_added_cutlery

    # Calculate the total number of pieces of cutlery in the drawer
    total_cutlery = total_forks + total_knives + total_spoons + total_teaspoons
    result = total_cutlery
    return result

print(solution())