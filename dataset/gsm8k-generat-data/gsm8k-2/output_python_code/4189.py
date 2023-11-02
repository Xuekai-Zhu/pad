def solution():
    """Marlon has a gift card for $200. He spent half of it on Monday and one-fourth of the remainder on Tuesday. How much was left on his gift card?"""
    gift_card = 200
    monday_spending = gift_card / 2
    remaining_amount = gift_card - monday_spending
    tuesday_spending = remaining_amount / 4
    remaining_amount -= tuesday_spending
    result = remaining_amount
    return result

print(solution())