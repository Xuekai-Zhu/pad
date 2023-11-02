def solution():
    """Maddy's 4th grade class needs to make 1000 Valentine's Day cards to get a pizza party. There are 30 kids in the class. If everyone makes 8, how many more cards will they need to make to get a pizza party?"""
    cards_per_student = 8
    total_students = 30
    cards_needed = 1000
    total_cards = cards_per_student * total_students
    cards_left_to_make = cards_needed - total_cards
    result = cards_left_to_make
    return result

print(solution())