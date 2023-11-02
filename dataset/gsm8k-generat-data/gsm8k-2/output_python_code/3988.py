def solution():
    """Ms. Jones got thank you cards from 30% of her class. 1/3 of these contained a gift card for $10. If she got $50 in gift cards, how many students were in her class?"""
    percent_thank_you = 0.3
    gift_card_percent = 1/3
    gift_card_value = 10
    total_gift_card_value = 50
    num_students = total_gift_card_value / (percent_thank_you * gift_card_percent * gift_card_value)
    result = num_students
    return result

print(solution())