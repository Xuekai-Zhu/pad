def solution():
    
    total_students = 28
    half_students = int(total_students / 2)
    half_with_5 = half_students * 5
    half_with_3 = half_students * 3
    total_notebooks = half_with_5 + half_with_3
    result = total_notebooks
    return result

print(solution())