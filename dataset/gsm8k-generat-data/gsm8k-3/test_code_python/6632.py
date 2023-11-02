def solution():
    """In soccer, players receive yellow cards when they are cautioned and red cards when they are sent off. Coach Tim has a team of 11 players, 5 of them didn't receive cautions, the rest received one yellow card each. How many red cards would the whole team collect, knowing that each red card corresponds to 2 yellow cards?"""
    # Define the number of players who did not receive cautions
    players_no_caution = 5

    # Define the number of players who received one yellow card each
    players_yellow_card = 11 - players_no_caution

    # Calculate the number of red cards that would be collected
    red_cards = players_yellow_card // 2

    # Display the number of red cards
    result = red_cards
    return result

print(solution())