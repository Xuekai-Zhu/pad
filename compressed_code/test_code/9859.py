def solution():
    
    total_students = 325
    glasses_percent = 40
    glasses_students = total_students * (glasses_percent / 100)
    no_glasses_students = total_students - glasses_students
    result = no_glasses_students
    return result

print(solution())