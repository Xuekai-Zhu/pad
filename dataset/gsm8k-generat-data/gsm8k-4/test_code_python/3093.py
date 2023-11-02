def solution():
    """Madeline wants to plant 20 flowers in her garden. She assumes that about half of the seeds she plants will die before they bloom. However, the flower shop only sells packs of seeds with 25 seeds per pack. Each pack is $5. How much will Madeline spend on seeds to plant 20 flowers?"""
    # Define the number of flowers Madeline wants to plant
    num_flowers = 20

    # Calculate the number of seeds needed, assuming half will die
    num_seeds = num_flowers * 2

    # Calculate the number of seed packets needed
    num_packs = num_seeds // 25
    if num_seeds % 25 != 0:
        num_packs += 1

    # Calculate the total cost of the seed packets
    total_cost = num_packs * 5

    # return the result
    result = total_cost
    return result

print(solution())