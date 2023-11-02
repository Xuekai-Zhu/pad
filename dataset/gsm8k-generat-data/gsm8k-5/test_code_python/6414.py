def solution():
    flies_per_frog = 30  # Each frog eats 30 flies per day
    frogs_per_fish = 8  # Each fish eats 8 frogs per day
    fish_per_gharial = 15  # Each gharial eats 15 fish per day
    gharials = 9  # There are 9 gharials in the swamp

    # Calculate the total number of fish needed to feed the gharials
    total_fish = gharials * fish_per_gharial

    # Calculate the total number of frogs needed to feed the fish
    total_frogs = total_fish * frogs_per_fish

    # Calculate the total number of flies needed to feed the frogs
    total_flies = total_frogs * flies_per_frog
    result = total_flies
    return result

print(solution())