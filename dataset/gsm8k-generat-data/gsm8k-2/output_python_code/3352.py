def solution():
    """Joseph gave 23 cards to each of his 15 students and had 12 cards left. How many cards did Joseph have at first?"""
    cards_per_student = 23
    total_students = 15
    left_over_cards = 12
    total_cards_given = cards_per_student * total_students + left_over_cards
    initial_cards = total_cards_given - left_over_cards
    result = initial_cards
    return result

print(solution())