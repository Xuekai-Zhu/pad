def solution():
    """Three schools organized a science fair competition and invited students from all the schools to develop ideas and present them before a panel of judges selected by all the schools competing in the science fair. There were 50 students from Know It All High School at the competition, 3/5 times as many students from Karen High as Know It All High School, and twice the combined number of students from the first two schools that came were from Novel Corona High School. Calculate the total number of students at the competition?"""
    know_it_all_students = 50
    karen_students = (3/5) * know_it_all_students
    novel_corona_students = 2 * (know_it_all_students + karen_students)
    total_students = know_it_all_students + karen_students + novel_corona_students
    result = total_students
    return result

print(solution())