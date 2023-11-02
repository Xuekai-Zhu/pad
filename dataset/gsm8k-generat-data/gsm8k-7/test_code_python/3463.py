def solution():
    num_christmas_cards = 20
    num_birthday_cards = 15
    card_cost = 2

    # Calculate the total number of cards bought
    total_cards = num_christmas_cards + num_birthday_cards

    # Calculate the total cost of all cards bought
    total_cost = total_cards * card_cost
    result = total_cost
    return result

print(solution())