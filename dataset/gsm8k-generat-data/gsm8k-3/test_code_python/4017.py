def solution():
    """Tom broke his leg and needed to go to the doctor.  The visit cost $300 and the cast cost $200. If insurance covered 60%, how much was Tom's out-of-pocket cost?"""
    # Define the costs and the insurance coverage percentage
    visit_cost = 300
    cast_cost = 200
    coverage_pct = 0.6  # 60%

    # Calculate the total cost before insurance coverage
    total_cost = visit_cost + cast_cost

    # Calculate the amount covered by insurance
    covered_amount = total_cost * coverage_pct

    # Calculate Tom's out-of-pocket cost
    out_of_pocket_cost = total_cost - covered_amount

    # Display Tom's out-of-pocket cost
    result = out_of_pocket_cost
    return result

print(solution())