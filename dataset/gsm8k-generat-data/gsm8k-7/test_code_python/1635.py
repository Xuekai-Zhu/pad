def solution():
    grades_semester_1 = [90, 80, 70, 100]
    average_semester_1 = sum(grades_semester_1) / len(grades_semester_1)
    
    average_semester_2 = 82
    
    # Calculate the difference in averages
    difference = average_semester_1 - average_semester_2
    result = difference
    return result

print(solution())