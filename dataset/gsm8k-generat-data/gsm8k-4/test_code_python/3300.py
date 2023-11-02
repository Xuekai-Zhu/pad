def solution():
    """Ivory got four more riddles than Josh did. Taso got twice as many riddles as Ivory did. If Josh has 8 riddles, how many riddles does Taso have?"""
    # Define the number of riddles that Josh has
    josh_riddles = 8

    # Calculate the number of riddles that Ivory has
    ivory_riddles = josh_riddles + 4

    # Calculate the number of riddles that Taso has
    taso_riddles = ivory_riddles * 2

    # return the result
    result = taso_riddles
    return result

print(solution())