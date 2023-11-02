def solution():
    
    tim_visit_cost = 300
    insurance_coverage = 0.75
    cat_visit_cost = 120
    cat_insurance_coverage = 60
    total_cost = tim_visit_cost * (1 - insurance_coverage) + \
        cat_visit_cost * (1 - cat_insurance_coverage / cat_visit_cost)
    result = total_cost
    return result

print(solution())