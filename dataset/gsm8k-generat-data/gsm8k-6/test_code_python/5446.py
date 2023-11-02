def solution():
    # Calculate the time to reach the 10th floor
    total_time = 0  # initialize total time
    for floor in range(2, 11):  # start from 2nd floor as 1st floor is already included, end at 10th floor
        if floor % 2 == 0: # even floor
            total_time += 15
        else: # odd floor
            total_time += 9
    
    # Convert total time to minutes
    minutes = total_time / 60
    result = minutes
    return result

print(solution())