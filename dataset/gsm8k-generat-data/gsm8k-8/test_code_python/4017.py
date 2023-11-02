def solution():
    # Calculate the total cost of the visit
    total_cost = 300 + 200

    # Calculate the amount covered by insurance
    insurance_covered = total_cost * 0.6

    # Calculate Tom's out-of-pocket cost
    out_of_pocket_cost = total_cost - insurance_covered
    result = out_of_pocket_cost
    return result

print(solution())