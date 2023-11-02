def solution():
    # Calculate the personal cost of replacing John's hearing aids
    total_cost = 2500 * 2  # cost of replacing both hearing aids
    insurance_coverage = 0.8  # insurance covers 80% of the cost
    covered_cost = total_cost * insurance_coverage  # cost covered by insurance
    personal_cost = total_cost - covered_cost  # personal cost of replacing the hearing aids
    result = personal_cost
    return result

print(solution())