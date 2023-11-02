def solution():
    """In one year, the number of students on campus doubles at the end of every month. If there are 10 students on campus at the beginning of the year, how many additional students would have joined by the end of May, above and beyond the number of students already on campus at the beginning of the year?"""
    starting_students = 10
    new_students = starting_students * 2 ** 5
    students_in_may = new_students - starting_students
    result = students_in_may
    return result

print(solution())