def solution():
    utensils_per_pack = 30  # Each pack contains 30 utensils
    spoons_per_pack = utensils_per_pack / 3  # Each pack contains an equal number of knives, forks, and spoons
    spoons_needed = 50  # John needs 50 spoons

    # Calculate the number of packs John needs to buy
    packs_needed = spoons_needed / spoons_per_pack
    result = packs_needed
    return result

print(solution())