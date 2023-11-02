def solution():
    
    total_students = 80
    perfect_scored = total_students * (2/5)
    remaining_students = total_students - perfect_scored
    over_80_scored = remaining_students * 0.5
    failed_students = total_students - (perfect_scored + over_80_scored)
    result = failed_students
    return result

print(solution())