def solution():
    """Miss Smith is teaching second period English and is shocked at how small the class seems. There are 6 tables in the classroom with 3 students currently sitting at each table. Sally said 3 girls went to the bathroom, and three times more students went to the canteen. Elliott said that 2 groups of students have recently been added to their class, and each group has 4 students in it. None of these students are in the class right now. Lucas pointed out that a few foreign exchange students have joined the class; 3 from Germany, 3 from France, and 3 from Norway. These students are also missing. How many students are supposed to be in the class?"""
    # Define the number of tables and the number of students per table
    TABLES = 6
    STUDENTS_PER_TABLE = 3

    # Calculate the total number of students from the tables
    total_students = TABLES * STUDENTS_PER_TABLE

    # Calculate the number of students that went to the canteen
    canteen_students = 3 * 3

    # Subtract the students that went to the bathroom and the canteen
    total_students -= (3 + canteen_students)

    # Add the recently added students
    total_students += (2 * 4)

    # Add the foreign exchange students
    total_students += (3 + 3 + 3)

    # return the result
    result = total_students
    return result

print(solution())