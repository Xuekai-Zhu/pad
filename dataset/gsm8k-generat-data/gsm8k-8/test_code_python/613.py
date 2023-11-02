def solution():
    # Define the cost of one hearing aid
    cost = 2500

    # Calculate the total cost of replacing both hearing aids
    total_cost = cost * 2

    # Calculate the amount covered by insurance
    insurance_coverage = total_cost * 0.8

    # Calculate the amount John personally has to pay
    personal_payment = total_cost - insurance_coverage
    result = personal_payment
    return result

print(solution())