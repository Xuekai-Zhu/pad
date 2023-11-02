def solution():
    num_flowers = 20
    seed_survival_rate = 0.5  # assume half of the seeds will die
    seeds_per_pack = 25
    pack_cost = 5

    # Calculate the total number of seeds needed
    total_seeds = num_flowers / seed_survival_rate

    # Calculate the total number of seed packs needed
    total_packs = total_seeds / seeds_per_pack

    # Round up the number of packs to an integer
    total_packs = math.ceil(total_packs)

    # Calculate the total cost of all seed packs
    total_cost = total_packs * pack_cost
    result = total_cost
    return result

print(solution())