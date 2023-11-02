def solution():
    
    total_students = 400
    sports_percent = 0.52
    soccer_percent = 0.125
    sports_students = total_students * sports_percent
    soccer_students = sports_students * soccer_percent
    result = soccer_students
    return result

print(solution())