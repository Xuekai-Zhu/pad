def solution():
    num_frogs_per_fish = 8
    num_flies_per_frog = 30
    num_fish_per_gharial = 15
    num_gharials = 9

    # Calculate the total number of fish needed to feed all the gharials
    total_fish_needed = num_fish_per_gharial * num_gharials

    # Calculate the total number of frogs needed to feed all the fish
    total_frogs_needed = num_frogs_per_fish * total_fish_needed

    # Calculate the total number of flies needed to feed all the frogs
    total_flies_needed = num_flies_per_frog * total_frogs_needed
    result = total_flies_needed
    return result

print(solution())