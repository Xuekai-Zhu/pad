def solution():
    
    # Define the length of a glass of milk and the number of glasses consumed
    GLASS_LENGTH = 8
    NUM_GLASSES = 2

    # Calculate the total length of milk consumed
    total_length = GLASS_LENGTH * NUM_GLASSES

    # Calculate the total number of calories consumed
    calories_consumed = total_length * 3

    # Display the total number of calories consumed
    result = calories_consumed
    return result

print(solution())