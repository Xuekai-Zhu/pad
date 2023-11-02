def solution():
    """Tom broke his leg and needed to go to the doctor. The visit cost $300 and the cast cost $200. If insurance covered 60% how much was Tom's out-of-pocket cost?"""
    visit_cost = 300
    cast_cost = 200
    insurance_coverage = 0.6
    total_cost = visit_cost + cast_cost
    covered_amount = total_cost * insurance_coverage
    out_of_pocket_cost = total_cost - covered_amount
    result = out_of_pocket_cost
    return result

print(solution())