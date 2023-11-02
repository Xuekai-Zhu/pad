def solution():
     students = 8
     construction_paper = 3
     glue = 6
     original_supplies = (students * construction_paper) + glue
     dropped_supplies = original_supplies / 2
     new_supplies = original_supplies - dropped_supplies + (construction_paper * 5)
     result = new_supplies
     return result

print(solution())