def solution():
    """To get admission into a school party, each football team member must pay $40. If there are 60 players on the football team and the entire team attends 8 such parties in a year, calculate the total amount of money collected in the 8 parties."""
    # Define the price of admission per player
    PRICE_PER_PLAYER = 40

    # Define the number of players on the football team
    num_players = 60

    # Define the number of parties the team attends
    num_parties = 8

    # Calculate the total amount of money collected
    total_money_collected = PRICE_PER_PLAYER * num_players * num_parties

    # Display the total amount of money collected
    result = total_money_collected
    return result

print(solution())