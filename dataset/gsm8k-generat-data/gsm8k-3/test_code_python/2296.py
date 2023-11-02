def solution():
    """Mancino is tending 3 gardens that each measure 16 feet by 5 feet. His sister, Marquita, is tilling the soil for two gardens that each measure 8 feet by 4 feet. How many square feet combined are in all their gardens?"""
    # Define the dimensions of Mancino's gardens and Marquita's gardens
    MANCINO_LENGTH = 16
    MANCINO_WIDTH = 5
    MARQUITA_LENGTH = 8
    MARQUITA_WIDTH = 4

    # Calculate the area of Mancino's gardens
    mancino_area = 3 * MANCINO_LENGTH * MANCINO_WIDTH

    # Calculate the area of Marquita's gardens
    marquita_area = 2 * MARQUITA_LENGTH * MARQUITA_WIDTH

    # Calculate the total area of all the gardens
    total_area = mancino_area + marquita_area

    # Display the total area
    result = total_area
    return result

print(solution())