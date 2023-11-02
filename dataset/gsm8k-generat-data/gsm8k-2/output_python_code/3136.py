def solution():
    """The math teacher would be happy if the class average test score was at least 85. There are 10 students in the class, 5 of which scored a 92 on the test and 4 of which scored an 80. What would the last student have to score to at least make the teacher happy?"""
    desired_average = 85
    num_students = 10
    current_total = (5 * 92) + (4 * 80)
    needed_total = num_students * desired_average
    last_student_score = needed_total - current_total
    result = last_student_score
    return result

print(solution())