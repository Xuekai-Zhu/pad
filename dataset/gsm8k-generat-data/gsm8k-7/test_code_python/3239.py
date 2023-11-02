def solution():
    property_damage = 40000
    medical_bills = 70000
    insurance_coverage = 0.8

    # Calculate the amount that Carl's insurance will cover
    property_coverage = property_damage * insurance_coverage
    medical_coverage = medical_bills * insurance_coverage

    # Calculate the amount that Carl personally owes
    property_remaining = property_damage - property_coverage
    medical_remaining = medical_bills - medical_coverage
    total_remaining = property_remaining + medical_remaining
    result = total_remaining
    return result

print(solution())