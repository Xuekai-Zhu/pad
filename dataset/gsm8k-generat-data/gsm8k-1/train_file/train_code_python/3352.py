def solution():
    """Joseph gave 23 cards to each of his 15 students and had 12 cards left. How many cards did Joseph have at first?"""
    cards_per_student = 23
    num_students = 15
    cards_left = 12
    total_cards_given = cards_per_student * num_students
    initial_cards = total_cards_given + cards_left
    result = initial_cards
    return result

print(solution())