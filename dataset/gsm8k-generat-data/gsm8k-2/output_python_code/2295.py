def solution():
    """Mancino is tending 3 gardens that each measure 16 feet by 5 feet. His sister, Marquita, is tilling the soil for two gardens that each measure 8 feet by 4 feet. How many square feet combined are in all their gardens?"""
    mancino_garden_area = 3 * (16 * 5)
    marquita_garden_area = 2 * (8 * 4)
    total_area = mancino_garden_area + marquita_garden_area
    result = total_area
    return result

print(solution())