def solution():
    """There were 200 students on a field playing football. Suddenly a military plane flew by, and 3/4 of the students looked up. How many eyes saw the airplane?"""
    total_students = 200
    looked_up_percent = 0.75
    total_look_up = total_students * looked_up_percent
    total_eyes = total_look_up * 2
    result = total_eyes
    return result

print(solution())