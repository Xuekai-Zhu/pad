def solution():
    """There were 200 students on a field playing football. Suddenly a military plane flew by, and 3/4 of the students looked up. How many eyes saw the airplane?"""
    total_students = 200
    looked_up = 0.75 * total_students
    eyes_that_saw = looked_up * 2 
    result = eyes_that_saw
    return result

print(solution())