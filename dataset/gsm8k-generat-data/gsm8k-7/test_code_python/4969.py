def solution():
    num_skirts = 3
    skirt_length = 12
    skirt_width = 4

    bodice_area = 2 + (5 * 2)  # shirt + 2 sleeves
    num_bodices = 1

    material_cost = 3  # dollars per square foot

    # Calculate the total area of the material needed for all skirts
    total_skirt_area = num_skirts * (skirt_length * skirt_width)

    # Calculate the total area of the material needed for the bodices
    total_bodice_area = num_bodices * bodice_area

    # Calculate the total area of material needed for the entire costume
    total_material_area = total_skirt_area + total_bodice_area

    # Calculate the total cost of the material
    total_cost = total_material_area * material_cost
    result = total_cost
    return result

print(solution())