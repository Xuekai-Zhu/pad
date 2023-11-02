def solution():
    period1_students = 11
    
    # Using the given information, we can write an equation in terms of period2_students
    # period1_students = 2*period2_students - 5
    # Solving for period2_students:
    period2_students = (period1_students + 5) / 2
    
    result = period2_students
    return result

print(solution())