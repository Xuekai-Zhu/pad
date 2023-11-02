def solution():
    total_fish = 90  # There are 90 fish in the exhibit
    swordfish_ratio = 5  # There are 5 times as many swordfish as pufferfish

    # Set up an equation to solve for the number of pufferfish
    # Let x be the number of pufferfish
    # Then 5x is the number of swordfish
    # And x + 5x = total_fish
    # Solving for x gives x = total_fish / 6
    num_pufferfish = total_fish / (swordfish_ratio + 1)
    result = num_pufferfish
    return result

print(solution())