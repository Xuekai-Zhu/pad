def solution():
    
    total_hands = 20
    hands_per_student = 2
    total_students = int(total_hands / hands_per_student) + 1
    result = total_students
    return result

print(solution())