def solution():
    weight = 30  # The child weighs 30 kilograms.
    full_dose = weight * 5  # For every kilogram of weight, the child must be given 5 ml of medicine.
    parts = 3  # The full dose has to be given in 3 equal parts.

    # Calculate the amount of medicine for each part of the dose
    part_dose = full_dose / parts
    result = part_dose
    return result

print(solution())