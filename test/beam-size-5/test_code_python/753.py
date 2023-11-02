def solution():
    
    small_students = 11
    medium_students = small_students * 2
    large_students = medium_students / 2
    extra_large_students = large_students + 6
    total_students = small_students + medium_students + large_students + extra_large_students
    result = total_students
    return result

print(solution())