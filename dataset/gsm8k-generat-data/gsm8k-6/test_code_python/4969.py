def solution():
    # Calculate the total area of material needed for the overskirt and petticoats
    skirt_area = 12 * 4  # area of material needed for one skirt
    total_skirt_area = skirt_area * 3  # area of material needed for three skirts

    # Calculate the area of material needed for the bodice
    bodice_area = 2 + (5 * 2)  # area of material needed for the bodice and sleeves

    # Calculate the total area of material needed for the whole costume
    total_area = total_skirt_area + bodice_area

    # Calculate the total cost of the material
    cost_per_square_foot = 3  # cost per square foot of material
    total_cost = total_area * cost_per_square_foot

    result = total_cost
    return result

print(solution())