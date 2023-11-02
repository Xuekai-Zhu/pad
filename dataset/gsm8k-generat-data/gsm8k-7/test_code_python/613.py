def solution():
    hearing_aid_cost = 2500
    insurance_coverage = 0.8

    # Calculate the total cost of both hearing aids
    total_cost = hearing_aid_cost * 2

    # Calculate the amount covered by insurance
    insurance_payment = total_cost * insurance_coverage

    # Calculate the amount that John has to pay
    personal_payment = total_cost - insurance_payment
    result = personal_payment
    return result

print(solution())