def solution():
    """Marlon has a gift card for $200. He spent half of it on Monday and one-fourth of the remainder on Tuesday. How much was left on his gift card?"""
    # Define the initial value of the gift card
    gift_card_value = 200

    # Calculate how much Marlon spent on Monday
    spent_on_monday = gift_card_value / 2

    # Calculate how much Marlon had left after spending on Monday
    remaining_after_monday = gift_card_value - spent_on_monday

    # Calculate how much Marlon spent on Tuesday
    spent_on_tuesday = remaining_after_monday / 4

    # Calculate how much Marlon had left after spending on Tuesday
    remaining_after_tuesday = remaining_after_monday - spent_on_tuesday

    # Display how much was left on Marlon's gift card
    result = remaining_after_tuesday
    return result

print(solution())