def solution():
    num_students = 15
    cards_per_student = 23
    cards_left = 12

    # Calculate the total number of cards given out
    total_cards_given = num_students * cards_per_student

    # Calculate the initial number of cards Joseph had
    initial_num_cards = total_cards_given + cards_left
    result = initial_num_cards
    return result

print(solution())