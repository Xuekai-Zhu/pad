def solution():
    
    semester1_grades = [90, 80, 70, 100]
    semester2_average = 82
    semester1_average = sum(semester1_grades) / len(semester1_grades)
    difference = semester1_average - semester2_average
    result = difference
    return result

print(solution())