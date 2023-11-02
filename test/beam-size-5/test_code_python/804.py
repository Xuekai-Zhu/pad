def solution():
    
    quarts_left = 10
    quarts_per_student_1 = 1.5
    quarts_per_student_2 = 2
    total_quarts_drunk = 4 * quarts_per_student_1 + 16 * quarts_per_student_2
    gallons_left = quarts_left - total_quarts_drunk
    result = gallons_left
    return result

print(solution())