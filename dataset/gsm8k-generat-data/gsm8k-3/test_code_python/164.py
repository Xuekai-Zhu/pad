def solution():
    """On Monday Buddy has 30 baseball cards. On Tuesday Buddy loses half of them. On Wednesday Buddy buys 12 baseball cards. On Thursday he buys a third of what he had on Tuesday. How many baseball cards does he have on Thursday?"""
    # Define the initial number of baseball cards
    initial_cards = 30

    # Calculate the number of baseball cards on Tuesday after losing half
    tuesday_cards = initial_cards / 2

    # Calculate the number of baseball cards on Wednesday after buying 12
    wednesday_cards = tuesday_cards + 12

    # Calculate the number of baseball cards on Thursday after buying a third of Tuesday's amount
    thursday_cards = tuesday_cards + (tuesday_cards / 3)

    result = thursday_cards
    return result

print(solution())