def solution():
    """To get admission into a school party, each football team member must pay $40. If there are 60 players on the football team and the entire team attends 8 such parties in a year, calculate the total amount of money collected in the 8 parties."""
    price_per_player = 40
    num_players = 60
    num_parties = 8
    total_money_collected = price_per_player * num_players * num_parties
    result = total_money_collected
    return result

print(solution())