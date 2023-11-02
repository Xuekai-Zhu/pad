def solution():
    """Tim's cat bit him. He decided to get himself and the cat checked out. His doctor's visits $300 and insurance covered 75%. His cat's visit cost $120 and his pet insurance covered $60. How much did he pay?"""
    tim_visit_cost = 300
    insurance_coverage = 0.75
    cat_visit_cost = 120
    cat_insurance_coverage = 60
    total_cost = tim_visit_cost * (1 - insurance_coverage) + \
        cat_visit_cost * (1 - cat_insurance_coverage / cat_visit_cost)
    result = total_cost
    return result

print(solution())