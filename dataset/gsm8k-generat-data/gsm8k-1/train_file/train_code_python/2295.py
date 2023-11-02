def solution():
    """Mancino is tending 3 gardens that each measure 16 feet by 5 feet. His sister, Marquita, is tilling the soil for two gardens that each measure 8 feet by 4 feet. How many square feet combined are in all their gardens?"""
    garden1_length = 16
    garden1_width = 5
    garden2_length = 16
    garden2_width = 5
    garden3_length = 16
    garden3_width = 5
    garden4_length = 8
    garden4_width = 4
    garden5_length = 8
    garden5_width = 4
    total_area = ((garden1_length * garden1_width) +(garden2_length * garden2_width) + (garden3_length * garden3_width)
                  + (garden4_length * garden4_width) + (garden5_length * garden5_width))
    result = total_area
    return result

print(solution())