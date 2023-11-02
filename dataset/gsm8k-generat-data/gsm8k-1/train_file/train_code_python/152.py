def solution():
    """Tim's cat bit him. He decided to get himself and the cat checked out. His doctor's visits $300 and insurance covered 75%. His cat's visit cost $120 and his pet insurance covered $60. How much did he pay?"""
    tim_visit = 300
    tim_insurance_coverage = 0.75
    tim_out_of_pocket = tim_visit * (1 - tim_insurance_coverage)
    cat_visit = 120
    cat_insurance_coverage = 60
    total_out_of_pocket = tim_out_of_pocket + cat_visit - cat_insurance_coverage
    result = total_out_of_pocket
    return result

print(solution())