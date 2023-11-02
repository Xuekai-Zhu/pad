def solution():
    num_jenny_cards = 6
    num_orlando_cards = num_jenny_cards + 2
    num_richard_cards = num_orlando_cards * 3

    # Calculate the total number of cards they have in all
    total_cards = num_jenny_cards + num_orlando_cards + num_richard_cards
    result = total_cards
    return result

print(solution())