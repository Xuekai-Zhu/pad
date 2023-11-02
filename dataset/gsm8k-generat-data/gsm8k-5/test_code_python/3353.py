def solution():
    cards_given_to_each_student = 23
    total_students = 15
    cards_left = 12

    # Calculate the total number of cards given to students
    total_cards_given = cards_given_to_each_student * total_students

    # Calculate the total number of cards Joseph had at first
    total_cards = total_cards_given + cards_left
    result = total_cards
    return result

print(solution())