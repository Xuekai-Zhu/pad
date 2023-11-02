def solution():
    
    seventh_grade_percent = 32
    sixth_grade_percent = 38
    total_students = int(64 / (seventh_grade_percent / 100))
    sixth_graders = int(total_students * (sixth_grade_percent / 100))
    result = sixth_graders
    return result

print(solution())