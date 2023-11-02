def solution():
    """The treasurer of a football team must buy equipment for the sixteen players of his team. Each piece of equipment consists of a $25 jersey, a $15.20 pair of shorts and a pair of socks at $6.80. How much does all the equipment of all the players on the team cost?"""
    num_players = 16
    jersey_cost = 25
    shorts_cost = 15.20
    socks_cost = 6.80
    total_cost = num_players * (jersey_cost + shorts_cost + socks_cost)
    result = total_cost
    return result

print(solution())