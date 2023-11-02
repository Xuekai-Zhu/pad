def solution():
    num_basketball_boxes = 4
    basketball_cards_per_box = 10
    num_baseball_boxes = 5
    baseball_cards_per_box = 8
    cards_given_to_classmates = 58

    # Calculate the total number of basketball cards that Ben has
    total_basketball_cards = num_basketball_boxes * basketball_cards_per_box

    # Calculate the total number of baseball cards that Ben has
    total_baseball_cards = num_baseball_boxes * baseball_cards_per_box

    # Calculate the total number of cards that Ben has before giving any to classmates
    total_cards = total_basketball_cards + total_baseball_cards

    # Calculate the number of cards that Ben has left after giving some to classmates
    cards_left = total_cards - cards_given_to_classmates
    result = cards_left
    return result

print(solution())