def solution():
    """Madeline wants to plant 20 flowers in her garden. She assumes that about half of the seeds she plants will die before they bloom. However, the flower shop only sells packs of seeds with 25 seeds per pack. Each pack is $5. How much will Madeline spend on seeds to plant 20 flowers?"""
    # Determine the number of seeds Madeline needs to plant
    total_seeds_needed = 20 * 2  # double the number of flowers to account for seeds that may die

    # Determine the number of seed packs Madeline needs to buy
    packs_needed = total_seeds_needed // 25
    if total_seeds_needed % 25 != 0:
        packs_needed += 1

    # Calculate the total cost of the seed packs
    total_cost = packs_needed * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())