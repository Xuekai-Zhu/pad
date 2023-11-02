def solution():
    """John ends up damaging his hearing aids. He needs to replace both of them. They cost $2500 each. Insurance covers 80% of the cost. How much does he personally have to pay?"""
    # Define the cost of each hearing aid and the insurance coverage
    cost_per_aid = 2500
    insurance_coverage = 0.8

    # Calculate the total cost of both hearing aids
    total_cost = cost_per_aid * 2

    # Calculate the amount covered by insurance
    insurance_amount = total_cost * insurance_coverage

    # Calculate the amount John has to pay out of pocket
    out_of_pocket = total_cost - insurance_amount

    # return the result
    result = out_of_pocket
    return result

print(solution())