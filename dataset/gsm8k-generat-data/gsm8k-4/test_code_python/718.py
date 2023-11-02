def solution():
    """Jake and Penny are hunting snakes. Jake's snake is 12 inches longer than Jenny's snake. If the two snakes have a combined length of 70 inches, how long is Jake's snake?"""
    # Define the length of Jenny's snake
    jenny_length = None

    # Define the difference in length between the two snakes
    difference = 12

    # Define the total length of both snakes
    total_length = 70

    # Solve for Jenny's snake length using substitution
    # jenny_length + jenny_length + difference = total_length
    # 2 * jenny_length = total_length - difference
    # jenny_length = (total_length - difference) / 2
    jenny_length = (total_length - difference) / 2
    
    # Calculate the length of Jake's snake
    jake_length = jenny_length + difference

    # return the result
    result = jake_length
    return result

print(solution())