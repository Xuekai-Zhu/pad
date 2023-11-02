def solution():
     students_surveyed = 450
     students_who_liked_oranges = 70
     students_who_liked_pears = 120
     students_who_liked_apples = 147
     students_who_liked_strawberries = students_surveyed - students_who_liked_oranges - students_who_liked_pears - students_who_liked_apples
     result = students_who_liked_strawberries
     return result

print(solution())