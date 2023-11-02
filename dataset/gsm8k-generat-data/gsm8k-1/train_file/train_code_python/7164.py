def solution():
    """A school has 1000 students. Half of the students were taken on a trip to the nearby beach. Half of the remaining students were sent home. How many students are still in the school?"""
    total_students = 1000
    students_on_beach = total_students / 2
    students_left = total_students - students_on_beach
    students_sent_home = students_left / 2
    students_remaining = students_left - students_sent_home
    result = students_remaining
    return result

print(solution())