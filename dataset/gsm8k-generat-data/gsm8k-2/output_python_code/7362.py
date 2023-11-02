def solution():
    """A class composed of 12 girls and 10 boys was sent to the library for their reading class. Their teacher found out that only 5/6 of the girls and 4/5 of the boys are reading. How many students are not reading?"""
    num_girls_reading = 5/6 * 12
    num_boys_reading = 4/5 * 10
    num_students_reading = num_girls_reading + num_boys_reading
    total_students = 12 + 10
    num_students_not_reading = total_students - num_students_reading
    result = num_students_not_reading
    return result

print(solution())