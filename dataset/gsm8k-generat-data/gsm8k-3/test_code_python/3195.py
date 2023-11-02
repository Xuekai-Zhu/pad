def solution():
    """James buys 5 packs of sodas that are 12 sodas each. He had 10 sodas already. He finishes all the sodas in 1 week. How many sodas does he drink a day?"""
    # Define the number of packs of sodas James buys
    packs_of_sodas = 5

    # Define the number of sodas per pack
    sodas_per_pack = 12

    # Calculate the total number of sodas James has
    total_sodas = packs_of_sodas * sodas_per_pack + 10

    # Calculate the number of sodas James drinks per day
    sodas_per_day = total_sodas / 7

    # Display the number of sodas James drinks per day
    result = sodas_per_day
    return result

print(solution())