def solution():
    """The fifth grade class at Rosa Parks Elementary School is holding a food drive. Half the students in Ms. Perez's class collected 12 cans each, two students didn't collect any, and the remaining 13 students students each collected 4 cans. If Ms. Perez's class has 30 students, how many cans did they collect total?"""
    # Define the number of students in Ms. Perez's class
    class_size = 30

    # Calculate the number of students who collected 12 cans
    twelve_cans_students = class_size // 2

    # Calculate the number of cans collected by those students
    twelve_cans = twelve_cans_students * 12

    # Calculate the number of students who didn't collect any cans
    no_cans_students = 2

    # Calculate the number of students who collected 4 cans
    four_cans_students = class_size - twelve_cans_students - no_cans_students

    # Calculate the number of cans collected by those students
    four_cans = four_cans_students * 4

    # Calculate the total number of cans collected
    total_cans = twelve_cans + four_cans

    # return the result
    result = total_cans
    return result

print(solution())