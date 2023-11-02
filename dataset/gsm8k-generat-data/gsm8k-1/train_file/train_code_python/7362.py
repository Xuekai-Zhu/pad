def solution():
    """A class composed of 12 girls and 10 boys was sent to the library for their reading class. Their teacher found out that only 5/6 of the girls and 4/5 of the boys are reading. How many students are not reading?"""
    num_girls_reading = int(5/6 * 12)
    num_boys_reading = int(4/5 * 10)
    num_girls_not_reading = 12 - num_girls_reading
    num_boys_not_reading = 10 - num_boys_reading
    total_students_not_reading = num_girls_not_reading + num_boys_not_reading
    result = total_students_not_reading
    return result

print(solution())