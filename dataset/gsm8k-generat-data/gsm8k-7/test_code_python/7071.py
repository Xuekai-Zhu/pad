def solution():
    num_new_cards = 8
    num_remaining_cards = 46
    # Calculate the number of cards that Keith started with
    num_starting_cards = (num_remaining_cards + num_new_cards) * 2
    result = num_starting_cards
    return result

print(solution())