def solution():
    """Tina buys 3 12-packs of soda for a party. Including Tina, 6 people are at the party. Half of the people at the party have 3 sodas each, 2 of the people have 4 and 1 person has 5. How many sodas are left over when the party is over?"""
    
    # Define the number of soda packs Tina buys and the number of sodas per pack
    soda_packs = 3
    sodas_per_pack = 12

    # Calculate the total number of sodas Tina buys
    total_sodas = soda_packs * sodas_per_pack

    # Calculate the total number of sodas consumed at the party
    total_consumed = (6/2) * 3 + 2*4 + 5

    # Calculate the number of sodas left over
    sodas_left = total_sodas - total_consumed

    # Return the result
    result = sodas_left
    return result

print(solution())