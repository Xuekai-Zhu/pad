def solution():
    """Jorge has an equal number of baseball cards as Matias, who has 6 fewer cards than Carlos.
    If Carlos has 20 baseball cards, what is the total number of baseball cards the three have?"""
    carlos_cards = 20
    matias_cards = carlos_cards - 6
    jorge_cards = matias_cards
    total_cards = carlos_cards + matias_cards + jorge_cards
    result = total_cards
    return result

print(solution())