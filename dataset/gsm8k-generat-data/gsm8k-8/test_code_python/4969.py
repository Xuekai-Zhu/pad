def solution():
    # Calculate the total material needed for the skirts
    skirt_area = (12 * 4) * 3

    # Calculate the material needed for the bodice and sleeves
    bodice_area = 2 + (5 * 2)

    # Calculate the total material needed
    total_material = skirt_area + bodice_area

    # Calculate the total cost of the material
    total_cost = total_material * 3
    result = total_cost
    return result

print(solution())