def solution():
    """James hurts himself and decides to go to his primary care doctor. His primary care doctor charges $300 for the visit and James's insurance covers 80%. What is James's out-of-pocket cost?"""
    # Define the cost of the visit
    visit_cost = 300

    # Calculate the amount covered by insurance
    insurance_covered = visit_cost * 0.8

    # Calculate James's out-of-pocket cost
    out_of_pocket_cost = visit_cost - insurance_covered

    # return the result
    result = out_of_pocket_cost
    return result

print(solution())