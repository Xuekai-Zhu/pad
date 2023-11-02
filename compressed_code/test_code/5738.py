def solution():
    
    total_students = 45
    under_11 = total_students / 3
    above_11_below_13 = (2 / 5) * total_students
    over_13 = total_students - under_11 - above_11_below_13
    result = over_13
    return result

print(solution())