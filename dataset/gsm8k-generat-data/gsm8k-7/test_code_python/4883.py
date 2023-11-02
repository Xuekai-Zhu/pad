def solution():
    mri_cost = 1200
    exam_time = 0.5  # 30 minutes
    exam_fee_per_hour = 300
    seen_fee = 150
    insurance_coverage = 0.8

    # Calculate the cost of the doctor's examination
    exam_cost = exam_fee_per_hour * (exam_time * 2)

    # Calculate the total cost before insurance coverage
    total_cost = mri_cost + exam_cost + seen_fee

    # Calculate the amount covered by insurance
    covered_amount = total_cost * insurance_coverage

    # Calculate the amount paid by Tim
    amount_paid = total_cost - covered_amount
    result = amount_paid
    return result

print(solution())