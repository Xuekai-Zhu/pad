def solution():
    """In soccer, players receive yellow cards when they are cautioned and red cards when they are sent off. Coach Tim has a team of 11 players, 5 of them didn't receive cautions, the rest received one yellow card each. How many red cards would the whole team collect, knowing that each red card corresponds to 2 yellow cards?"""
    total_players = 11
    players_without_cautions = 5
    players_with_cautions = total_players - players_without_cautions
    yellow_cards = players_with_cautions
    red_cards = yellow_cards / 2
    result = red_cards
    return result

print(solution())