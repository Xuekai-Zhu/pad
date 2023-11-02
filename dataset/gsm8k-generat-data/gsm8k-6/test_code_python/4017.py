def solution():
    # Calculate the total cost of the visit
    total_cost = 300 + 200

    # Calculate the amount covered by insurance
    covered_amount = total_cost * 0.6

    # Calculate Tom's out-of-pocket cost
    out_of_pocket = total_cost - covered_amount
    result = out_of_pocket
    return result

print(solution())