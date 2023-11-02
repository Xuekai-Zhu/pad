def solution():
    # Define the ratio of quilts to yards of material
    quilt_to_material_ratio = 7 / 21

    # Use the ratio to calculate how many yards of material are needed for 1 quilt
    one_quilt_material = 1 / quilt_to_material_ratio

    # Use the previous calculation to find how many yards of material are needed for 12 quilts
    material_for_12_quilts = one_quilt_material * 12
    result = material_for_12_quilts
    return result

print(solution())