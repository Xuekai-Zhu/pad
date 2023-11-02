def solution():
    spoons_per_pack = 30 // 3   # Each pack has an equal number of knives, forks, and spoons
    num_spoons_needed = 50
    num_packs_needed = (num_spoons_needed // spoons_per_pack) + (num_spoons_needed % spoons_per_pack > 0)  # Round up to the nearest pack
    result = num_packs_needed
    return result

print(solution())