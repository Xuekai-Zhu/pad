def solution():
    tablecloth_length = 102
    tablecloth_width = 54
    napkin_length = 6
    napkin_width = 7
    num_napkins = 8

    # Calculate the area of the tablecloth
    tablecloth_area = tablecloth_length * tablecloth_width

    # Calculate the area of one napkin
    napkin_area = napkin_length * napkin_width

    # Calculate the total area of all the napkins
    total_napkin_area = num_napkins * napkin_area

    # Calculate the total area of material needed
    total_area = tablecloth_area + total_napkin_area
    result = total_area
    return result

print(solution())