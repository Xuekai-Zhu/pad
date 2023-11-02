def solution():
    """Rob has 24 baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. How many doubles baseball cards does Jess have?"""
    # Calculate the number of doubles in Rob's collection
    rob_doubles = 24 / 3

    # Calculate the number of doubles in Jess's collection
    jess_doubles = rob_doubles * 5

    # Display the number of doubles in Jess's collection
    result = jess_doubles
    return result

print(solution())