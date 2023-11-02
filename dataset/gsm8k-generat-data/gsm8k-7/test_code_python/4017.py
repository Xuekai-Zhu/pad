def solution():
    visit_cost = 300
    cast_cost = 200
    insurance_coverage = 0.6  # 60% coverage

    # Calculate the total cost before insurance coverage
    total_cost = visit_cost + cast_cost

    # Calculate the amount covered by insurance
    insurance_payment = total_cost * insurance_coverage

    # Calculate Tom's out-of-pocket cost
    out_of_pocket_cost = total_cost - insurance_payment
    result = out_of_pocket_cost
    return result

print(solution())