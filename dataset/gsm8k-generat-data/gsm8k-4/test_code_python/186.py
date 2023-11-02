def solution():
    """Christina has 3 snakes. 1 snake is 2 feet long. Another snake is 16 inches long. The last snake is 10 inches long. How many inches are all of her snakes combined?"""
    # Define the length of each snake in inches
    snake1_length = 2 * 12 * 2.54 # Convert 2 feet to inches
    snake2_length = 16
    snake3_length = 10

    # Calculate the total length of all snakes in inches
    total_length = snake1_length + snake2_length + snake3_length
    
    # Return the result
    result = total_length
    return result

print(solution())