def solution():
    total_people = 13 + 3 + 2  # Roger needs to provide snack for 13 players, 3 coaches, and 2 helpers
    pouches_per_pack = 6  # Each pack of trail mix contains 6 individual pouches

    # Calculate the total number of pouches required
    total_pouches = total_people * 1.5  # Each person gets 1.5 pouches of trail mix

    # Calculate the number of packs of trail mix required
    packs_of_trail_mix = total_pouches / pouches_per_pack

    result = packs_of_trail_mix
    return result

print(solution())