def solution():
     """There are 40 students in a class. If 1/10 are absent, 3/4 of the students who are present are in the classroom, and the rest are in the canteen, how many students are in the canteen?"""
     students_in_class = 40
     absent_students = students_in_class / 10
     present_students = students_in_class - absent_students
     students_in_classroom = present_students * (3/4)
     students_in_canteen = present_students - students_in_classroom
     result = students_in_canteen
     return result

print(solution())