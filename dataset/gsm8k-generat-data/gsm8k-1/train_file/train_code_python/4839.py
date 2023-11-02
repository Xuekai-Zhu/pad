def solution():
    """Noel bakes 4 dozen donuts for his class. There are 30 students in class, but only 80% like donuts. How many donuts does each student who likes donuts get to eat?"""
    donut_per_dozen = 12
    total_donuts = 4 * donut_per_dozen
    students_in_class = 30
    like_donuts_percent = 80
    donut_eating_students = students_in_class * (like_donuts_percent / 100)
    donuts_per_student = total_donuts / donut_eating_students
    result = donuts_per_student
    return result

print(solution())