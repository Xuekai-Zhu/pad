def solution():
    """Jorge has an equal number of baseball cards as Matias, who has 6 fewer cards than Carlos. If Carlos has 20 baseball cards, what is the total number of baseball cards the three have?"""
    # Define the number of cards Carlos has
    carlos_cards = 20

    # Calculate the number of cards Matias has
    matias_cards = carlos_cards - 6

    # Calculate the number of cards Jorge has
    jorge_cards = matias_cards

    # Calculate the total number of cards the three have
    total_cards = carlos_cards + matias_cards + jorge_cards

    # return the result
    result = total_cards
    return result

print(solution())