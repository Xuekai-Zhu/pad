def solution():
    """Marlon has a gift card for $200. He spent half of it on Monday and one-fourth of the remainder on Tuesday. How much was left on his gift card?"""
    initial_amount = 200
    monday_spending = initial_amount / 2
    remaining_amount = initial_amount - monday_spending
    tuesday_spending = remaining_amount / 4
    remaining_amount = remaining_amount - tuesday_spending
    result = remaining_amount
    return result

print(solution())