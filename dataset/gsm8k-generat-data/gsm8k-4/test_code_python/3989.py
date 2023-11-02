def solution():
    """Ms. Jones got thank you cards from 30% of her class. 1/3 of these contained a gift card for $10. If she got $50 in gift cards, how many students were in her class?"""
    # Define the percentage of students who gave thank you cards and the fraction of these that contained a gift card
    thank_you_percentage = 0.3
    gift_card_fraction = 1/3

    # Calculate the number of thank you cards that contained a gift card
    gift_card_count = thank_you_percentage * gift_card_fraction

    # Calculate the value of the gift cards received
    gift_card_value = gift_card_count * 10

    # Calculate the total number of students in the class
    total_students = gift_card_value / 50 * 100

    # return the result
    result = total_students
    return result

print(solution())