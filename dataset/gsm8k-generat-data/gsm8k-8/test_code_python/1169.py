def solution():
    # Calculate the total number of basketball cards
    num_basketball_cards = 4 * 10

    # Calculate the total number of baseball cards
    num_baseball_cards = 5 * 8

    # Calculate the total number of cards Ben started with
    total_cards = num_basketball_cards + num_baseball_cards

    # Subtract the cards he gave away to find the remaining amount
    remaining_cards = total_cards - 58
    result = remaining_cards
    return result

print(solution())