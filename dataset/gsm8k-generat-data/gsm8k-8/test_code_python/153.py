def solution():
    # Calculate the amount of Tim's doctor visit that insurance did not cover
    doctor_cost = 300
    insurance_coverage = 0.75
    uncovered_doctor_cost = doctor_cost * (1 - insurance_coverage)

    # Calculate the amount of Tim's cat's vet visit that insurance did not cover
    cat_cost = 120
    cat_insurance_coverage = 60
    uncovered_cat_cost = cat_cost - cat_insurance_coverage

    # Calculate the total amount Tim paid
    total_cost = uncovered_doctor_cost + uncovered_cat_cost
    result = total_cost
    return result

print(solution())