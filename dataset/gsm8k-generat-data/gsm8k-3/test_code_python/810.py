def solution():
    """Tyler has 21 CDs. He gives away a third of his CDs to his friend. Then he goes to the music store and buys 8 brand new CDs. How many CDs does Tyler have now?"""
    # Define the initial number of CDs and the fraction given away
    initial_cds = 21
    fraction_given_away = 1/3

    # Calculate the number of CDs given away and remaining
    given_away = int(initial_cds * fraction_given_away)
    remaining = initial_cds - given_away

    # Calculate the final number of CDs after buying new ones
    final_cds = remaining + 8

    # Display the final number of CDs
    result = final_cds
    return result

print(solution())