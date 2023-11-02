def solution():
    """Ashton had two boxes of pencils with fourteen pencils in each box. He gave six pencils to his brother. How many pencils did Ashton have left?"""
    # Define the initial number of pencils
    initial_num_pencils = 2 * 14

    # Define the number of pencils given to Ashton's brother
    brother_pencils = 6

    # Calculate the number of pencils Ashton has left
    left_pencils = initial_num_pencils - brother_pencils

    # Display the number of pencils Ashton has left
    result = left_pencils
    return result

print(solution())