def solution():
    """Rob has some baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. If Jess has 40 doubles baseball cards, how many baseball cards does Rob have?"""
    # Calculate the number of doubles Rob has
    rob_doubles = 40 / 5

    # Calculate the total number of cards Rob has
    rob_total = rob_doubles / (1/3)

    # Display the total number of cards Rob has
    result = rob_total
    return result

print(solution())