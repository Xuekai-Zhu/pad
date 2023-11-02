def solution():
    saplings_per_3spears = 1
    logs_per_9spears = 1
    
    num_saplings = 6
    num_logs = 1
    
    # Calculate the total number of spears Marcy can make from saplings
    num_spears_from_saplings = (num_saplings // saplings_per_3spears) * 3

    # Calculate the total number of spears Marcy can make from logs
    num_spears_from_logs = (num_logs // logs_per_9spears) * 9
    
    # Calculate the total number of spears Marcy can make
    total_num_spears = num_spears_from_saplings + num_spears_from_logs
    result = total_num_spears
    return result

print(solution())