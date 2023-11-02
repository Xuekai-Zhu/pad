def solution():
    # Define the given variables
    cards_per_student = 23
    num_students = 15
    leftover_cards = 12

    # Calculate the total number of cards given out
    total_cards_given = cards_per_student * num_students + leftover_cards

    # Calculate how many cards Joseph had at first
    initial_cards = total_cards_given - leftover_cards
    result = initial_cards
    return result

print(solution())