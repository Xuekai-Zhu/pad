def solution():
    tables = 6  # There are 6 tables in the classroom
    students_per_table = 3  # There are 3 students at each table
    missing_students = 3 + (3*3) + (2*4)  # 3 students in the bathroom, 3 times more went to canteen, and 2 groups of 4 students each were recently added
    foreign_students = 3+3+3  # 3 foreign exchange students each from Germany, France, and Norway
    total_students = (tables * students_per_table) + missing_students + foreign_students
    result = total_students
    return result

print(solution())