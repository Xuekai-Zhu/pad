def solution():
    
    initial_boys = 15
    initial_girls = round(initial_boys * 1.2)
    total_students = initial_boys + initial_girls
    final_girls = initial_girls * 2
    total_students += final_girls - initial_girls
    result = total_students
    return result

print(solution())