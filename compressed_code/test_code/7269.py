def solution():
    
    total_students = 20
    in_classroom = total_students // 4
    on_playground = total_students - in_classroom
    boys_on_playground = on_playground // 3
    girls_on_playground = on_playground - boys_on_playground
    result = girls_on_playground
    return result

print(solution())