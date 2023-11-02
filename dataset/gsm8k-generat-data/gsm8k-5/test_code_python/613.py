def solution():
    cost_per_aid = 2500  # The cost of each hearing aid is $2500
    insurance_coverage = 0.8  # Insurance covers 80% of the cost

    # Calculate the total cost of replacing both hearing aids
    total_cost = 2 * cost_per_aid

    # Calculate how much of the total cost insurance will cover
    insurance_payment = insurance_coverage * total_cost

    # Calculate how much John will have to pay personally
    personal_payment = total_cost - insurance_payment
    result = personal_payment
    return result

print(solution())