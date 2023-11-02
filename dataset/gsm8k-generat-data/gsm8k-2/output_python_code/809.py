def solution():
    """Tyler has 21 CDs. He gives away a third of his CDs to his friend. Then he goes to the music store and buys 8 brand new CDs. How many CDs does Tyler have now?"""
    initial_cds = 21
    given_away_cds = initial_cds / 3
    remaining_cds = initial_cds - given_away_cds
    new_cds = 8
    total_cds = remaining_cds + new_cds
    result = total_cds
    return result

print(solution())