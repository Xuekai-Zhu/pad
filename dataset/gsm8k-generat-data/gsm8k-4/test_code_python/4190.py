def solution():
    """Marlon has a gift card for $200. He spent half of it on Monday and one-fourth of the remainder on Tuesday. How much was left on his gift card?"""
    # Define the initial amount on the gift card
    initial_amount = 200

    # Calculate the amount spent on Monday
    monday_spending = initial_amount / 2

    # Calculate the amount remaining after Monday
    remaining_amount = initial_amount - monday_spending

    # Calculate the amount spent on Tuesday
    tuesday_spending = remaining_amount / 4

    # Calculate the amount remaining after Tuesday
    remaining_amount -= tuesday_spending

    result = remaining_amount
    return result

print(solution())