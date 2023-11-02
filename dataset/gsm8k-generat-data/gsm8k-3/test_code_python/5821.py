def solution():
    """James hurts himself and decides to go to his primary care doctor.  His primary care doctor charges $300 for the visit and James's insurance covers 80%.  What is James's out-of-pocket cost?"""
    # Define the cost of the doctor's visit
    VISIT_COST = 300

    # Define the insurance coverage rate
    INSURANCE_COVERAGE = 0.8

    # Calculate James's out-of-pocket cost
    out_of_pocket_cost = VISIT_COST * (1 - INSURANCE_COVERAGE)

    # Display James's out-of-pocket cost
    result = out_of_pocket_cost
    return result

print(solution())