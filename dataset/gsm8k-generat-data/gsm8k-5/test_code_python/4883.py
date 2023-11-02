def solution():
    mri_cost = 1200  # Cost of the MRI
    exam_time = 0.5  # Time (in hours) for the doctor to examine the MRI
    exam_cost = 300  # Cost per hour for the doctor's examination
    seen_cost = 150  # Fee for being seen by the doctor
    insurance_coverage = 0.8  # Insurance covers 80% of the total cost

    # Calculate the total cost of the doctor's visit
    total_cost = mri_cost + (exam_time * exam_cost) + seen_cost

    # Calculate the out-of-pocket cost for Tim after insurance coverage
    out_of_pocket_cost = total_cost * (1 - insurance_coverage)
    result = out_of_pocket_cost
    return result

print(solution())