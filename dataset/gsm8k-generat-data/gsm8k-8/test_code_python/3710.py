def solution():
    # Define variables
    num_students = 4
    total_distance = 200
    
    # Calculate the average completion time of all four runners
    average_time_all = 30
    
    # Calculate the total time taken by all four runners
    total_time_all = num_students * average_time_all
    
    # Calculate the total time taken by the last three runners
    total_time_last_three = (num_students-1) * 35
    
    # Calculate the time taken by the first student
    time_first_student = total_time_all - total_time_last_three
    
    result = time_first_student
    return result

print(solution())