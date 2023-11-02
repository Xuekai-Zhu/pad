def solution():
    num_cards_needed = 1000
    num_students = 30
    cards_per_student = 8

    # Calculate the total number of cards that the students can make
    total_cards = num_students * cards_per_student

    # Calculate the difference between the total number of cards and the number needed
    difference = num_cards_needed - total_cards
    result = difference
    return result

print(solution())