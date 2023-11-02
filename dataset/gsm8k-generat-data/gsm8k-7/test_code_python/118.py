def solution():
    start_num_objects = 3
    num_weeks = 5
    
    # Calculate the total number of objects Jeanette can juggle after 5 weeks
    total_num_objects = start_num_objects
    for i in range(1, num_weeks):
        total_num_objects += (start_num_objects + i)
    
    result = total_num_objects
    return result

print(solution())