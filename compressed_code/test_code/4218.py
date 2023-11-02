def solution():
    
    total_students = 30
    half_students = total_students/2
    cans_per_half = 12
    no_cans_students = 2
    cans_per_remaining = 4
    total_cans = (half_students * cans_per_half) + (total_students - half_students - no_cans_students) * cans_per_remaining
    result = total_cans
    return result

print(solution())