def solution():
     class_size = 250
     present_girls = 140
     present_students = present_girls * 2
     absent_students = class_size - present_students
     absent_boys = absent_students / 2
     
     return absent_boys

print(solution())