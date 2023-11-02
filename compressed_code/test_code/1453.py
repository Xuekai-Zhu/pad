def solution():
    
    total_students = 20
    classroom_students = total_students // 4
    playground_students = total_students - classroom_students
    boys_playground_students = playground_students // 3
    girls_playground_students = playground_students - boys_playground_students
    result = girls_playground_students
    return result

print(solution())