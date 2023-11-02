def solution():
    doctor_charge = 300  # The primary care doctor charges $300 for the visit
    insurance_coverage = 0.8  # James's insurance covers 80% of the charge

    # Calculate the amount covered by James's insurance
    insurance_payment = doctor_charge * insurance_coverage

    # Calculate James's out-of-pocket cost
    out_of_pocket_cost = doctor_charge - insurance_payment
    result = out_of_pocket_cost
    return result

print(solution())