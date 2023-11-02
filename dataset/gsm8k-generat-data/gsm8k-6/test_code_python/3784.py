def solution():
    # Calculate the total area of the tablecloth
    tablecloth_area = 102 * 54

    # Calculate the total area of 1 napkin
    napkin_area = 6 * 7

    # Calculate the total area of 8 napkins
    napkins_total_area = 8 * napkin_area

    # Calculate the total square inches of material needed
    total_material_area = tablecloth_area + napkins_total_area
    result = total_material_area
    return result

print(solution())