def solution():
    # Calculate the number of boxes of football cards
    football_boxes = 9 - 3

    # Calculate the total number of football cards
    football_cards = football_boxes * 20

    # Calculate the total number of basketball cards
    basketball_cards = 9 * 15

    # Calculate the total number of cards
    total_cards = football_cards + basketball_cards
    result = total_cards
    return result

print(solution())