def solution():
    """A school has 1000 students. Half of the students were taken on a trip to the nearby beach. Half of the remaining students were sent home. How many students are still in the school?"""
    total_students = 1000
    beach_students = total_students / 2
    remaining_students = total_students - beach_students
    sent_home_students = remaining_students / 2
    remaining_students = remaining_students - sent_home_students
    result = remaining_students
    return result

print(solution())