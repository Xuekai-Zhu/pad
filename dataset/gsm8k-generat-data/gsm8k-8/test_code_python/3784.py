def solution():
    # Calculate the area of the tablecloth
    tablecloth_area = 102 * 54

    # Calculate the area of one napkin
    napkin_area = 6 * 7

    # Calculate the total area of all 8 napkins
    total_napkin_area = napkin_area * 8

    # Calculate the total area of material needed
    total_material_area = tablecloth_area + total_napkin_area

    result = total_material_area
    return result

print(solution())