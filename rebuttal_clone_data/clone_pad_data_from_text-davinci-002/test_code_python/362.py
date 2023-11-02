def solution():
    tote_weight = 8
    briefcase_weight = tote_weight / 2
    laptop_weight = briefcase_weight
    papers_weight = briefcase_weight / 6
    full_briefcase_weight = laptop_weight + papers_weight
 
    result = full_briefcase_weight - tote_weight
    return result

print(solution())