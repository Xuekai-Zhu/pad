def solution():
    # Define the cost of the primary care visit and the insurance coverage percentage
    visit_cost = 300
    insurance_coverage = 0.8

    # Calculate James's out-of-pocket cost
    out_of_pocket_cost = visit_cost * (1 - insurance_coverage)
    result = out_of_pocket_cost
    return result

print(solution())