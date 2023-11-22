def solution():
    
    # Define the depth of the water on Monday
    monday_depth = 17

    # Define the depth of the water on Tuesday
    tuesday_depth = monday_depth + 7

    # Define the depth of the water on Wednesday
    wednesday_depth = tuesday_depth * (2/3)

    # Display the depth of the water on Wednesday
    result = wednesday_depth
    return result

print(solution())