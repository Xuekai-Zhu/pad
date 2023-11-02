def solution():
    # Find the number of thank you cards Ms. Jones received
    thank_you_cards = 0.3 * x  # where x is the number of students in her class

    # Find the number of thank you cards containing a gift card
    gift_card_cards = (1/3) * thank_you_cards

    # Find the total value of the gift cards
    total_gift_cards = 10 * gift_card_cards

    # Find the number of students in her class
    students = total_gift_cards / 50

    result = students
    return result

print(solution())