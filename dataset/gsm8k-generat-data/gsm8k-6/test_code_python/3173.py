def solution():
    # Calculate the total number of baseball cards Phil bought in a year
    total_cards = 20 * 52  # he buys 20 cards per week for 52 weeks in a year

    # Calculate the number of cards Phil lost in the fire
    lost_cards = total_cards / 2  # he lost half of the cards

    # Calculate the number of cards Phil has left
    remaining_cards = total_cards - lost_cards

    result = remaining_cards
    return result

print(solution())