def solution():
    """A Statistics student wants to find out the average daily allowance of the middle school students. According to his survey, 2/3 of the students receive an average of $6 allowance per day while the rest gets an average of $4 a day. If he surveyed 60 students, what is the total amount of money those 60 students get in a day?"""
    total_students = 60
    students_with_6_allowance = total_students * (2/3)
    students_with_4_allowance = total_students - students_with_6_allowance
    allowance_from_6_students = students_with_6_allowance * 6
    allowance_from_4_students = students_with_4_allowance * 4
    total_allowance = allowance_from_6_students + allowance_from_4_students
    result = total_allowance
    return result

print(solution())