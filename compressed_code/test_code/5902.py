def solution():
    
    tim_visit = 300
    tim_insurance_coverage = 0.75
    tim_out_of_pocket = tim_visit * (1 - tim_insurance_coverage)
    cat_visit = 120
    cat_insurance_coverage = 60
    total_out_of_pocket = tim_out_of_pocket + cat_visit - cat_insurance_coverage
    result = total_out_of_pocket
    return result

print(solution())