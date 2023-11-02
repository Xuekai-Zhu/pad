def solution():
    total_cards = 500  # Marco has a total of 500 cards
    duplicates = total_cards / 4  # A fourth of the cards are duplicates
    traded_duplicates = duplicates / 5  # Marco trades one-fifth of the duplicates

    # Calculate the number of new cards Marco gets
    new_cards = traded_duplicates

    result = new_cards
    return result

print(solution())