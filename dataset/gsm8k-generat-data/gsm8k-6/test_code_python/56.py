def solution():
    # Find out the total time Leo worked on his assignment
    total_time = 2 * 60  # 2 hours in minutes
    
    # Calculate the time Leo spent on the second part of the assignment
    second_part_time = 2 * 25  # it took him twice as long as the first part
    
    # Calculate the time Leo spent on the third part of the assignment
    third_part_time = total_time - 25 - second_part_time
    
    result = third_part_time
    return result

print(solution())