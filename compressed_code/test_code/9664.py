def solution():
    
    total_students = 300
    full_scholarships = 0.05 * total_students
    half_scholarships = 0.1 * total_students
    no_scholarships = total_students - (full_scholarships + half_scholarships)
    result = no_scholarships
    return result

print(solution())