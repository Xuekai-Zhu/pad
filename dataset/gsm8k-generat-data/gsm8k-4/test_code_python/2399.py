def solution():
    """Rob has 24 baseball cards, and a few are doubles. One third of Rob's cards are doubles, and Jess has 5 times as many doubles as Rob. How many doubles baseball cards does Jess have?"""
    # Define the total number of cards Rob has and the ratio of doubles
    total_cards = 24
    double_ratio = 1/3

    # Calculate the number of doubles Rob has
    rob_doubles = total_cards * double_ratio

    # Calculate the number of doubles Jess has (5 times as many as Rob)
    jess_doubles = rob_doubles * 5

    result = jess_doubles
    return result

print(solution())