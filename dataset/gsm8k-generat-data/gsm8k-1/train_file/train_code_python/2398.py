def solution():
    """Rob has 24 baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. How many doubles baseball cards does Jess have?"""
    rob_cards = 24
    rob_doubles = rob_cards / 3
    jess_doubles = rob_doubles * 5
    result = jess_doubles
    return result

print(solution())