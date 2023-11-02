def solution():
    """In soccer, players receive yellow cards when they are cautioned and red cards when they are sent off. Coach Tim has a team of 11 players, 5 of them didn't receive cautions, the rest received one yellow card each. How many red cards would the whole team collect, knowing that each red card corresponds to 2 yellow cards?"""
    # Define the number of players on the team
    players = 11

    # Define the number of players who didn't receive cautions
    no_cautions = 5

    # Calculate the number of players who received cautions
    cautioned_players = players - no_cautions

    # Calculate the number of yellow cards given
    yellow_cards = cautioned_players

    # Calculate the number of red cards given
    red_cards = yellow_cards // 2

    result = red_cards
    return result

print(solution())