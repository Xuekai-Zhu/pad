def solution():
    
    # Define the size of the top level sandcastle
    top_level_size = 16

    # Calculate the size of each level sandcastle
    level_size = top_level_size / 2

    # Calculate the total size of the sandcastles
    total_size = level_size * 4

    # Calculate the average size of a level
    average_size = total_size / 4

    # Display the average size of a level
    result = average_size
    return result

print(solution())