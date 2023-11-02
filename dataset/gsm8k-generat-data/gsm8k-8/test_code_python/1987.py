def solution():
    # Define the total number of cards and the fraction that are red
    total_cards = 120
    red_fraction = 2/5

    # Calculate the number of red cards
    red_cards = red_fraction * total_cards

    # Calculate the number of non-red cards
    non_red_cards = total_cards - red_cards

    # Calculate the fraction of non-red cards that are black
    black_fraction = 5/9

    # Calculate the number of black cards
    black_cards = black_fraction * non_red_cards

    # Calculate the number of green cards
    green_cards = total_cards - red_cards - black_cards
    result = green_cards
    return result

print(solution())