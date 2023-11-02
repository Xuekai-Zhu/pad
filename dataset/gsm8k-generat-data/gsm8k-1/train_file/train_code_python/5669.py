def solution():
    """Miss Smith is teaching second period English and is shocked at how small the class seems. There are 6 tables in the classroom with 3 students currently sitting at each table. Sally said 3 girls went to the bathroom, and three times more students went to the canteen. Elliott said that 2 groups of students have recently been added to their class, and each group has 4 students in it. None of these students are in the class right now. Lucas pointed out that a few foreign exchange students have joined the class; 3 from Germany, 3 from France, and 3 from Norway. These students are also missing. How many students are supposed to be in the class?"""
    tables = 6
    students_per_table = 3
    currently_present = tables * students_per_table
    girls_in_bathroom = 3
    students_in_canteen = 3 * 3
    groups_added = 2 * 4
    foreign_students = 3 + 3 + 3
    total_students = currently_present + students_in_canteen + groups_added + foreign_students - girls_in_bathroom
    result = total_students
    return result

print(solution())