def solution():
    """James hurts himself and decides to go to his primary care doctor. His primary care doctor charges $300 for the visit and James's insurance covers 80%. What is James's out-of-pocket cost?"""
    doctor_charge = 300
    insurance_coverage = 0.8
    out_of_pocket_cost = doctor_charge * (1 - insurance_coverage)
    result = out_of_pocket_cost
    return result

print(solution())