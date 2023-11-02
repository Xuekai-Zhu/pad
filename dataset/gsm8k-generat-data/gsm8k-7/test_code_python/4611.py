def solution():
    initial_num_students = 160
    num_new_students = 20
    fraction_transfered = 1/3
    
    # Calculate the total number of students in Hendrix's class after the new students joined
    total_num_students = initial_num_students + num_new_students
    
    # Calculate the number of students that transferred out
    num_transfered = fraction_transfered * total_num_students
    
    # Calculate the number of students that remained at the end of the school year
    num_remaining = total_num_students - num_transfered
    result = num_remaining
    return result

print(solution())