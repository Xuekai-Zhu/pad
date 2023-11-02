def solution():
    """Miss Smith is teaching second period English and is shocked at how small the class seems. There are 6 tables in the classroom with 3 students currently sitting at each table. Sally said 3 girls went to the bathroom, and three times more students went to the canteen. Elliott said that 2 groups of students have recently been added to their class, and each group has 4 students in it. None of these students are in the class right now. Lucas pointed out that a few foreign exchange students have joined the class; 3 from Germany, 3 from France, and 3 from Norway. These students are also missing. How many students are supposed to be in the class?"""
    # Define the number of tables and students per table
    tables = 6
    students_per_table = 3

    # Calculate the total number of students sitting at tables
    total_students = tables * students_per_table

    # Subtract the number of students who went to the bathroom
    total_students -= 3

    # Add the number of students who went to the canteen
    total_students += 3 * 3

    # Add the number of students who were added to the class
    total_students += 2 * 4

    # Add the number of foreign exchange students who joined the class
    total_students += 3 + 3 + 3

    # Display the total number of students in the class
    result = total_students
    return result

print(solution())