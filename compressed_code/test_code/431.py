def solution():
    
    cards_per_student = 8
    total_students = 30
    cards_needed = 1000
    total_cards = cards_per_student * total_students
    cards_left_to_make = cards_needed - total_cards
    result = cards_left_to_make
    return result

print(solution())