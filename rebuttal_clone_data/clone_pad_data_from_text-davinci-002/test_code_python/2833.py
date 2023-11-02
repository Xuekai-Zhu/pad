def solution():
     class_one_preference = 1/6
     class_two_preference = 2/3
     class_three_preference = 1/5
     class_one_students = 30
     class_two_students = 30
     class_three_students = 30
     total_goldfish_preference = (class_one_preference * class_one_students) + (class_two_preference * class_two_students) + (class_three_preference * class_three_students)
     result = total_goldfish_preference
     return result

print(solution())