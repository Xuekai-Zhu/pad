def solution():
    
    initial_boys = 15
    initial_girls = int(initial_boys * 1.2)
    new_girls = initial_girls * 2
    new_students = new_girls + initial_boys
    result = new_students
    return result

print(solution())