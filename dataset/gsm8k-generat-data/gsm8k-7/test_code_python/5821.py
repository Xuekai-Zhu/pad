def solution():
    visit_cost = 300
    insurance_coverage = 0.8

    # Calculate the portion of the visit cost that is covered by James's insurance
    insurance_paid = visit_cost * insurance_coverage

    # Calculate James's out-of-pocket cost
    out_of_pocket = visit_cost - insurance_paid
    result = out_of_pocket
    return result

print(solution())