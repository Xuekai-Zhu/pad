def solution():
    """Tina buys 3 12-packs of soda for a party.  Including Tina, 6 people are at the party.  Half of the people at the party have 3 sodas each, 2 of the people have 4 and 1 person has 5.  How many sodas are left over when the party is over?"""
    # Define the number of 12-packs of soda Tina buys
    NUM_PACKS = 3

    # Define the number of sodas per pack
    SODAS_PER_PACK = 12

    # Calculate the total number of sodas Tina has for the party
    total_sodas = NUM_PACKS * SODAS_PER_PACK

    # Calculate the number of people who have 3 sodas each
    num_threes = 0.5 * 6

    # Calculate the total number of sodas consumed by the people who have 3 sodas each
    sodas_threes = num_threes * 3

    # Calculate the total number of sodas consumed by the people who have 4 sodas each
    sodas_fours = 2 * 4

    # Calculate the total number of sodas consumed by the person who has 5 sodas
    sodas_fives = 5

    # Calculate the total number of sodas consumed
    total_sodas_consumed = sodas_threes + sodas_fours + sodas_fives

    # Calculate the number of sodas left over
    sodas_left_over = total_sodas - total_sodas_consumed

    # Display the number of sodas left over
    result = sodas_left_over
    return result

print(solution())