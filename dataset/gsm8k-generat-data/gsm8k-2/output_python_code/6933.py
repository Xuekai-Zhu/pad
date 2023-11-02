def solution():
    """On the first day of school, Mrs. McGillicuddy had 25 students registered for the morning session of kindergarten,
    but 3 students were absent; and she had 24 students registered for the afternoon session,
    but 4 students were absent. How many students did Mrs. McGillicuddy have over the two kindergarten sessions?"""
    morning_reg = 25
    morning_absent = 3
    afternoon_reg = 24
    afternoon_absent = 4
    total_students = (morning_reg - morning_absent) + (afternoon_reg - afternoon_absent)
    result = total_students
    return result

print(solution())