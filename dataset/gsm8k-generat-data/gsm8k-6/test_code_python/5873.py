def solution():
    # Calculate the number of boys and girls per classroom
    boys_per_classroom = 56/4  
    girls_per_classroom = 44/4 

    # Calculate the total number of students per classroom
    total_students = boys_per_classroom + girls_per_classroom
    result = total_students
    return result

print(solution())