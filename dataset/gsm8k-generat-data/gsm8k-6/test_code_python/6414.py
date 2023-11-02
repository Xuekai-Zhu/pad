def solution():
    # Calculate the total number of flies eaten by 9 gharials
    flies_per_frog = 30  # each frog eats 30 flies a day
    frogs_per_fish = 8  # each fish eats 8 frogs a day
    fish_per_gharial = 15  # each gharial eats 15 fish a day
    gharials = 9  # there are 9 gharials in the swamp
    total_fish = gharials * fish_per_gharial  # total fish needed by 9 gharials
    total_frogs = total_fish * frogs_per_fish  # total frogs needed for the fish to eat
    total_flies = total_frogs * flies_per_frog  # total flies eaten by all animals
    result = total_flies
    return result

print(solution())