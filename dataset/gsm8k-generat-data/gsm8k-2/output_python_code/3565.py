def solution():
    """A class has 60 students. The number of students who bring their lunch is thrice the number of those who eat in the school cafeteria. The rest of the students don't eat lunch. If 10 students eat in the school cafeteria, how many don't eat lunch?"""
    total_students = 60
    cafeteria_students = 10
    lunch_bringers = 3 * cafeteria_students
    no_lunch_students = total_students - cafeteria_students - lunch_bringers
    result = no_lunch_students
    return result

print(solution())