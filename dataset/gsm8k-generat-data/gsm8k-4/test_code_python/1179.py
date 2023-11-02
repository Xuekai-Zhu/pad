def solution():
    """Rob has some baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. If Jess has 40 doubles baseball cards, how many baseball cards does Rob have?"""
    # Define the number of doubles that Rob has
    rob_doubles = None

    jess_doubles = 40

    # Calculate the total number of cards that Jess has
    jess_total = jess_doubles / (1/3)

    # Calculate the total number of cards that Rob has
    rob_total = (jess_total - jess_doubles) / 5

    result = rob_total
    return result

print(solution())