def solution():
    """Steven has 4 times as many shirts as Andrew. Andrew has 6 times as many shirts as Brian. If Brian has 3 shirts, how many does Steven have?"""
    # Define the number of shirts that Brian has
    brian_shirts = 3

    # Calculate the number of shirts that Andrew has
    andrew_shirts = 6 * brian_shirts

    # Calculate the number of shirts that Steven has
    steven_shirts = 4 * andrew_shirts

    # Display the number of shirts that Steven has
    result = steven_shirts
    return result

print(solution())