def solution():
    
    # Define the length of each quarter in minutes
    QUARTER_LENGTH = 12

    # Calculate the total length of the four quarters in minutes
    total_length = 4 * QUARTER_LENGTH * 4

    # Calculate the length of the last quarter in minutes
    last_quarter_length = total_length - 5

    # Display the length of the entire game
    result = last_quarter_length
    return result

print(solution())