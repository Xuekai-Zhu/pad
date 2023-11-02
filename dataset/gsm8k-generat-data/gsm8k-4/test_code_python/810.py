def solution():
    """Tyler has 21 CDs. He gives away a third of his CDs to his friend. Then he goes to the music store and buys 8 brand new CDs. How many CDs does Tyler have now?"""
    # Define the initial number of CDs
    initial_cds = 21

    # Calculate the number of CDs given away to a friend
    given_away_cds = initial_cds // 3

    # Calculate the remaining number of CDs
    remaining_cds = initial_cds - given_away_cds

    # Calculate the final number of CDs
    final_cds = remaining_cds + 8

    result = final_cds
    return result

print(solution())