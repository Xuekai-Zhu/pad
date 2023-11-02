def solution():
    
    tote_weight = 8
    briefcase_weight = tote_weight / 2
    briefcase_with_stuff_weight = tote_weight * 2
    laptop_and_papers_weight = briefcase_with_stuff_weight - briefcase_weight
    laptop_weight = laptop_and_papers_weight * (1 - (1/6))
    weight_difference = laptop_weight - tote_weight
    result = weight_difference
    return result

print(solution())