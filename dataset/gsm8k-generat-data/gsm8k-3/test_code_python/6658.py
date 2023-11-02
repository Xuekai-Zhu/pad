def solution():
    """Anna ate 4 apples on Tuesday. On Wednesday, she ate double the apples she ate on Tuesday. On Thursday, Anna ate half the apples she ate on Tuesday. How many apples has Anna eaten by the end of these three days?"""
    # Initialize the number of apples Anna has eaten
    apples_eaten = 4

    # Add the number of apples Anna ate on Wednesday
    apples_eaten += 2 * 4

    # Add the number of apples Anna ate on Thursday
    apples_eaten += 4 / 2

    # Display the total number of apples Anna has eaten
    result = apples_eaten
    return result

print(solution())