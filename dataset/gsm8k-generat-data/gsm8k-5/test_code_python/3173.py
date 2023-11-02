def solution():
    cards_per_week = 20  # Phil buys 20 cards each week
    weeks_per_year = 52  # Phil buys cards for 52 weeks in a year

    total_cards = cards_per_week * weeks_per_year  # Calculate the total number of cards Phil has in a year
    lost_cards = total_cards / 2  # Phil loses half of his cards in a fire

    remaining_cards = total_cards - lost_cards  # Calculate the number of remaining cards

    result = remaining_cards
    return result

print(solution())