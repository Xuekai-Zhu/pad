def solution():
    total_flowers = 20  # Madeline wants to plant 20 flowers
    seed_per_flower = 2  # Madeline needs to plant 2 seeds per flower to account for expected deaths
    total_seeds = total_flowers * seed_per_flower  # Madeline needs to plant this many seeds
    seeds_per_pack = 25  # Each pack of seeds contains 25 seeds
    packs_required = total_seeds // seeds_per_pack + int(total_seeds % seeds_per_pack > 0)  # Round up to the nearest pack
    pack_cost = 5  # Each pack of seeds costs $5

    # Calculate the total cost of the packs of seeds
    total_cost = packs_required * pack_cost
    result = total_cost
    return result

print(solution())