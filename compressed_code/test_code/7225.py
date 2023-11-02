def solution():
    
    students = 8
    paper_per_student = 3
    glue_bottles = 6
    total_paper = students * paper_per_student + glue_bottles
    lost_supplies = total_paper / 2
    additional_paper = 5
    remaining_supplies = total_paper - lost_supplies + additional_paper
    result = remaining_supplies
    return result

print(solution())