def solution():
    """Mancino is tending 3 gardens that each measure 16 feet by 5 feet. His sister, Marquita, is tilling the soil for two gardens that each measure 8 feet by 4 feet. How many square feet combined are in all their gardens?"""
    # Define the size of each of Mancino's gardens and calculate the total area
    mancino_garden_size = 16 * 5
    total_mancino_area = 3 * mancino_garden_size

    # Define the size of each of Marquita's gardens and calculate the total area
    marquita_garden_size = 8 * 4
    total_marquita_area = 2 * marquita_garden_size

    # Calculate the combined area of all the gardens
    total_area = total_mancino_area + total_marquita_area

    # return the result
    result = total_area
    return result

print(solution())