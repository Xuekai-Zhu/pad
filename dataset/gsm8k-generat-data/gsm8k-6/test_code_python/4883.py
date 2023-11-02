def solution():
    # Calculate total cost of doctor's visit
    exam_fee = 150  # fee for being seen
    mri_cost = 1200  # cost of MRI
    doctor_fee = 300 * 0.5  # 30-minute exam at $300 per hour
    total_cost = exam_fee + mri_cost + doctor_fee

    # Calculate Tim's out-of-pocket cost after insurance
    insurance_coverage = 0.8  # insurance covers 80% of the cost
    out_of_pocket_cost = total_cost * (1 - insurance_coverage)
    result = out_of_pocket_cost
    return result

print(solution())