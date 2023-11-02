def solution():
    """Rob has 24 baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. How many doubles baseball cards does Jess have?"""
    rob_total_cards = 24
    rob_double_cards = rob_total_cards / 3
    jess_double_cards = 5 * rob_double_cards
    result = jess_double_cards
    return result

print(solution())