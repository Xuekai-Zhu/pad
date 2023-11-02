def solution():
    carlos_cards = 20  # Carlos has 20 baseball cards
    matias_cards = carlos_cards - 6  # Matias has 6 fewer cards than Carlos
    jorge_cards = matias_cards  # Jorge has an equal number of cards as Matias

    # Calculate the total number of cards the three have
    total_cards = carlos_cards + matias_cards + jorge_cards
    result = total_cards
    return result

print(solution())