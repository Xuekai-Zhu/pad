def solution():
    # Calculate the number of thank you cards Ms. Jones received
    thank_you_cards = 0.3 * total_students

    # Calculate the number of thank you cards with gift cards
    gift_cards = thank_you_cards / 3

    # Calculate the total value of the gift cards
    gift_card_value = gift_cards * 10

    # Calculate the total number of students in Ms. Jones' class
    total_students = round(gift_card_value / 50 * 100)

    result = total_students
    return result

print(solution())