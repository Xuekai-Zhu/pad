def solution():
    
    total_students = 60
    percent_below_B = 40
    percent_above_B = 100 - percent_below_B
    students_above_B = total_students * (percent_above_B / 100)
    result = students_above_B
    return result

print(solution())