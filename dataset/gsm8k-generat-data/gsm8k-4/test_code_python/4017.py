def solution():
    """Tom broke his leg and needed to go to the doctor. The visit cost $300 and the cast cost $200. If insurance covered 60% how much was Tom's out-of-pocket cost?"""
    # Define the costs of the doctor's visit and the cast
    visit_cost = 300
    cast_cost = 200

    # Calculate the total cost of the visit
    total_cost = visit_cost + cast_cost

    # Calculate the amount covered by insurance
    insurance_coverage = total_cost * 0.6

    # Calculate Tom's out-of-pocket cost
    out_of_pocket_cost = total_cost - insurance_coverage

    # return the result
    result = out_of_pocket_cost
    return result

print(solution())