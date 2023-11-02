def solution():
    """Miss Smith is teaching second period English and is shocked at how small the class seems. There are 6 tables in the classroom with 3 students currently sitting at each table. Sally said 3 girls went to the bathroom, and three times more students went to the canteen. Elliott said that 2 groups of students have recently been added to their class, and each group has 4 students in it. None of these students are in the class right now. Lucas pointed out that a few foreign exchange students have joined the class; 3 from Germany, 3 from France, and 3 from Norway. These students are also missing. How many students are supposed to be in the class?"""
    tables = 6
    students_per_table = 3
    current_students = tables * students_per_table
    missing_from_bathroom = 3
    missing_from_canteen = 3 * 3
    missing_from_groups = 2 * 4 * 2
    missing_from_foreign_exchange = 3 * 3
    total_missing = missing_from_bathroom + missing_from_canteen + missing_from_groups + missing_from_foreign_exchange
    total_students = current_students + total_missing
    result = total_students
    return result

print(solution())