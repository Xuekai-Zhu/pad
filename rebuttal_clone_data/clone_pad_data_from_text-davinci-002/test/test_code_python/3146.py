def solution():
     total_students = 40
     glass_wearing_students = total_students * 0.25
     contact_wearing_students = total_students * 0.4
     non_vision_students = total_students - (glass_wearing_students + contact_wearing_students)
     result = non_vision_students
     return result

print(solution())