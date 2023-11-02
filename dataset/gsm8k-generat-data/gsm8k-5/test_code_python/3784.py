def solution():
    # Calculate the area of the tablecloth
    area_tablecloth = 102 * 54

    # Calculate the area of one napkin
    area_napkin = 6 * 7

    # Calculate the total area of all eight napkins
    total_area_napkins = area_napkin * 8

    # Calculate the total area of material needed
    total_area = area_tablecloth + total_area_napkins
    result = total_area
    return result

print(solution())