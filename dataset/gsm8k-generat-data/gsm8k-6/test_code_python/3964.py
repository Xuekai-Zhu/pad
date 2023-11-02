def solution():
    # Calculate maximum capacity of the conference center
    max_capacity = 6 * 80  # six rooms and each can hold up to 80 people
    
    # Calculate number of people in the conference center
    current_capacity = (2/3) * max_capacity
    
    result = current_capacity
    return result

print(solution())