def solution():
    """Jed collects stamp cards. Every week, he gets 6 cards. But every two weeks, he gives 2 cards to his friends. If Jed started with 20 cards, after how many weeks will he have a total of 40 cards?"""
    # Define Jed's initial number of cards and the target number of cards
    initial_cards = 20
    target_cards = 40

    # Initialize the number of weeks and remaining cards
    weeks = 0
    remaining_cards = initial_cards

    # Keep collecting cards until we reach the target number
    while remaining_cards < target_cards:
        # Increment the week counter
        weeks += 1

        # Collect 6 cards
        remaining_cards += 6

        # If it's been 2 weeks, give away 2 cards
        if weeks % 2 == 0:
            remaining_cards -= 2

    # Return the number of weeks it took to reach the target
    result = weeks
    return result

print(solution())