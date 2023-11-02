def solution():
    
    total_students = 300
    full_scholarship_percent = 0.05
    half_scholarship_percent = 0.1
    full_scholarship_count = total_students * full_scholarship_percent
    half_scholarship_count = total_students * half_scholarship_percent
    no_scholarship_count = total_students - full_scholarship_count - half_scholarship_count
    result = no_scholarship_count
    return result

print(solution())