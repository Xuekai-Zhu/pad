def solution():
    """Sally needs to make a tablecloth that measures 102 inches by 54 inches. She also needs to make 8 napkins that are 6 by 7 inches. How many square inches of material will Sally need to make the tablecloth and the 8 napkins?"""
    tablecloth_area = 102 * 54
    napkin_area = 8 * (6 * 7)
    total_area = tablecloth_area + napkin_area
    result = total_area
    return result

print(solution())