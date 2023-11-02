def solution():
    # Calculate the total amount of material produced by the three machines in 23 hours
    material_3 = 3 * 23 * 2  # 3 machines working 23 hours can produce 138 kg of material

    # Calculate the amount of material produced by the fourth machine in 12 hours
    material_4 = 1 * 12 * 2  # 1 machine working 12 hours can produce 24 kg of material

    # Calculate the total amount of material produced by all four machines in one day
    total_material = material_3 + material_4

    # Calculate the total income earned by selling the produced material
    total_income = total_material * 50  # the factory sells the produced material for $50 per 1 kg

    result = total_income
    return result

print(solution())