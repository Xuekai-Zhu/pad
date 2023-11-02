def solution():
    """Jed collects stamp cards. Every week, he gets 6 cards. But every two weeks, he gives 2 cards to his friends. If Jed started with 20 cards, after how many weeks will he have a total of 40 cards?"""
    # Define the initial number of cards and the target number of cards
    start_cards = 20
    target_cards = 40

    # Define the number of cards Jed gets and gives away each week
    get_cards = 6
    give_cards = 2

    # Initialize the number of weeks
    weeks = 0

    # Increment the number of weeks until the target number of cards is reached
    while start_cards < target_cards:
        weeks += 1
        start_cards += get_cards
        if weeks % 2 == 0:
            start_cards -= give_cards

    # Display the number of weeks
    result = weeks
    return result

print(solution())