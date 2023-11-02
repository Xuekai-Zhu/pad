def solution():
    """Ms. Jones got thank you cards from 30% of her class. 1/3 of these contained a gift card for $10. If she got $50 in gift cards, how many students were in her class?"""
    # Define the percentage of students who sent thank you cards and the fraction of those that contained gift cards
    THANK_YOU_PERCENTAGE = 0.3
    GIFT_CARD_FRACTION = 1/3

    # Calculate the number of students who sent thank you cards and the number of those that contained gift cards
    thank_you_count = THANK_YOU_PERCENTAGE * class_size
    gift_card_count = thank_you_count * GIFT_CARD_FRACTION

    # Calculate the total amount of gift card money Ms. Jones received
    gift_card_money = gift_card_count * 10

    # Calculate the remaining gift card money after deducting $50
    remaining_gift_card_money = gift_card_money - 50

    # Calculate the number of students in Ms. Jones' class
    class_size = round(thank_you_count / THANK_YOU_PERCENTAGE)

    # Display the number of students in Ms. Jones' class
    result = class_size
    return result

print(solution())