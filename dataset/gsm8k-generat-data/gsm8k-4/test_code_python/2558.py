def solution():
    """James can make a beret from 3 spools of yarn. If he has 12 spools of red yarn, 15 spools of black yarn,
    and 6 spools of blue yarn, how many berets can he make?"""
    # Define the number of spools of yarn needed to make a beret
    SPOOLS_PER_BERET = 3

    # Calculate the number of berets that can be made from each color of yarn
    red_berets = 12 // SPOOLS_PER_BERET
    black_berets = 15 // SPOOLS_PER_BERET
    blue_berets = 6 // SPOOLS_PER_BERET

    # Choose the smallest number of berets that can be made, based on the available yarn
    num_berets = min(red_berets, black_berets, blue_berets)

    result = num_berets
    return result

print(solution())