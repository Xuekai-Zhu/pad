def solution():
    """Paolo has 14 coconuts, while Dante has thrice as many coconuts as Paolo. If Dante sold 10 of his coconuts, how many coconuts did he have left?"""
    # Define the number of coconuts Paolo has
    paolo_coconuts = 14

    # Define the number of coconuts Dante has
    dante_coconuts = paolo_coconuts * 3

    # Subtract 10 from Dante's coconuts after selling
    dante_coconuts -= 10

    # Return the number of coconuts Dante has left
    result = dante_coconuts
    return result

print(solution())