def solution():
    """Rob has some baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. If Jess has 40 doubles baseball cards, how many baseball cards does Rob have?"""
    jess_doubles = 40
    rob_doubles = jess_doubles / 5
    total_cards = rob_doubles / (1/3)
    result = total_cards
    return result

print(solution())