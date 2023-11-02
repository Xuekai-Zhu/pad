def solution():
    num_basketball_decks = 6
    basketball_cards_per_deck = 25
    num_baseball_boxes = 5
    baseball_cards_per_box = 40
    cards_kept = 50
    cards_per_student = 10

    # Calculate the total number of basketball cards
    total_basketball_cards = num_basketball_decks * basketball_cards_per_deck

    # Calculate the total number of baseball cards
    total_baseball_cards = num_baseball_boxes * baseball_cards_per_box

    # Calculate the total number of cards
    total_cards = total_basketball_cards + total_baseball_cards

    # Calculate the number of cards remaining
    cards_remaining = total_cards - cards_kept

    # Calculate the number of students
    num_students = cards_remaining // cards_per_student
    result = num_students
    return result

print(solution())