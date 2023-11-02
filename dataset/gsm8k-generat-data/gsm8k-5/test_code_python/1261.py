def solution():
    total_cakes = 12  # Chastity made 12 cakes
    half_cakes = total_cakes / 2  # Half of the stack was knocked over by the crow
    undamaged_cakes = half_cakes / 2  # Chastity picked up half of the fallen cakes, which were undamaged
    destroyed_cakes = total_cakes - undamaged_cakes  # The rest of the cakes were destroyed

    result = destroyed_cakes
    return result

print(solution())