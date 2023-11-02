def solution():
    """On the first day of school, Mrs. McGillicuddy had 25 students registered for the morning session of kindergarten, but 3 students were absent; and she had 24 students registered for the afternoon session, but 4 students were absent. How many students did Mrs. McGillicuddy have over the two kindergarten sessions?"""
    morning_registered = 25
    morning_absent = 3
    afternoon_registered = 24
    afternoon_absent = 4
    students_present = morning_registered - morning_absent + afternoon_registered - afternoon_absent
    result = students_present
    return result

print(solution())