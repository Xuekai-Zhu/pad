def solution():
    """Ms. Jones got thank you cards from 30% of her class. 1/3 of these contained a gift card for $10. If she got $50 in gift cards, how many students were in her class?"""
    percent_received = 0.3
    percent_with_gift_card = 1/3
    amount_received = 50
    gift_card_amount = 10
    total_students = amount_received / (percent_received * percent_with_gift_card * gift_card_amount)
    result = total_students
    return result

print(solution())