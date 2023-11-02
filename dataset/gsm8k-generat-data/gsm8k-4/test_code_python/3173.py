def solution():
    """Phil likes to collect baseball cards. He buys a pack of twenty each week for a year, but then loses half of them one day in a fire. How many baseball cards does Phil have left?"""
    # Define the number of weeks in a year
    WEEKS_IN_YEAR = 52

    # Define the initial number of baseball cards
    initial_cards = 0

    # Calculate the total number of baseball cards collected in a year
    for week in range(WEEKS_IN_YEAR):
        initial_cards += 20

    # Calculate the remaining number of baseball cards after losing half in a fire
    remaining_cards = initial_cards / 2

    result = remaining_cards
    return result

print(solution())