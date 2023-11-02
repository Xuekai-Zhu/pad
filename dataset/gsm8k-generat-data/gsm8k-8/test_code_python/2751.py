def solution():
    # Define the number of cards Carlos has
    carlos_cards = 20

    # Define the number of cards Matias has
    matias_cards = carlos_cards - 6

    # Define the number of cards Jorge has
    jorge_cards = matias_cards

    # Calculate the total number of cards the three have
    total_cards = carlos_cards + matias_cards + jorge_cards
    result = total_cards
    return result

print(solution())