def solution():
    """Sally needs to make a tablecloth that measures 102 inches by 54 inches. She also needs to make 8 napkins that are 6 by 7 inches. How many square inches of material will Sally need to make the tablecloth and the 8 napkins?"""
    # Calculate the area of the tablecloth
    tablecloth_area = 102 * 54

    # Calculate the area of each napkin
    napkin_area = 6 * 7

    # Calculate the total area of all 8 napkins
    total_napkin_area = napkin_area * 8

    # Calculate the total area of material needed
    total_area = tablecloth_area + total_napkin_area

    result = total_area
    return result

print(solution())