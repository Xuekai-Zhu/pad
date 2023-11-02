def solution():
    """Paolo has 14 coconuts, while Dante has thrice as many coconuts as Paolo. If Dante sold 10 of his coconuts, how many coconuts did he have left?"""
    # Define the number of coconuts Paolo has
    paolo_coconuts = 14

    # Define the number of coconuts Dante has (3 times as many as Paolo)
    dante_coconuts = 3 * paolo_coconuts

    # Calculate the number of coconuts Dante has left after selling 10
    dante_coconuts_left = dante_coconuts - 10

    # Display the number of coconuts Dante has left
    result = dante_coconuts_left
    return result

print(solution())