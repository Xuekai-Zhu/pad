def solution():
    weight = 30
    dosage = 5  # ml per kg
    full_dose = weight * dosage
    num_parts = 3
    part_dose = full_dose / num_parts
    result = part_dose
    return result

print(solution())