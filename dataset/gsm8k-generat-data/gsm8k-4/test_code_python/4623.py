def solution():
    """Steven has 4 times as many shirts as Andrew. Andrew has 6 times as many shirts as Brian.
    If Brian has 3 shirts, how many does Steven have?"""
    # Define the initial number of shirts for Brian
    brian_shirts = 3

    # Calculate the number of shirts for Andrew
    andrew_shirts = brian_shirts * 6

    # Calculate the number of shirts for Steven
    steven_shirts = andrew_shirts * 4

    # Return the result
    result = steven_shirts
    return result

print(solution())