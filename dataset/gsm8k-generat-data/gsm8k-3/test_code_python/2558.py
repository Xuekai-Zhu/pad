def solution():
    """James can make a beret from 3 spools of yarn. If he has 12 spools of red yarn, 15 spools of black yarn, and 6 spools of blue yarn, how many berets can he make?"""
    # Define the number of spools of yarn needed per beret
    YARN_PER_BERET = 3

    # Calculate the number of berets that can be made from each color
    red_berets = 12 // YARN_PER_BERET
    black_berets = 15 // YARN_PER_BERET
    blue_berets = 6 // YARN_PER_BERET

    # Determine the maximum number of berets that can be made
    max_berets = min(red_berets, black_berets, blue_berets)

    # Display the maximum number of berets that can be made
    result = max_berets
    return result

print(solution())