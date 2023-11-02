def solution():
    """Rory has 30 more jellybeans than her sister Gigi who has 15 jellybeans. Lorelai has already eaten three times the number of jellybeans that both girls have. How many jellybeans has Lorelai eaten?"""
    gigi_jellybeans = 15
    rory_jellybeans = gigi_jellybeans + 30
    total_jellybeans = gigi_jellybeans + rory_jellybeans
    lorelai_jellybeans = total_jellybeans * 3
    result = lorelai_jellybeans
    return result

print(solution())