def solution():
    """Cary is saving money to buy a new pair of shoes that cost $120. He has already saved $30. He earns $5 for every lawn he mows. If he mows 3 lawns each weekend, how many more weekends will he have to mow lawns before he can afford to buy the shoes?"""
    # Define the cost of the shoes and the amount of money Cary has already saved
    SHOE_COST = 120
    SAVED_MONEY = 30

    # Define Cary's earnings per lawn mowed
    LAWN_EARNINGS = 5

    # Calculate the amount of money Cary still needs to save
    remaining_money = SHOE_COST - SAVED_MONEY

    # Calculate how many lawns Cary needs to mow to reach the remaining money goal
    lawns_needed = remaining_money / LAWN_EARNINGS

    # Calculate how many weekends Cary needs to mow 3 lawns to reach the lawns_needed goal
    weekends_needed = lawns_needed / 3

    # Round up the result to the nearest whole number of weekends
    weekends_needed = int(round(weekends_needed + 0.5))

    # Display how many more weekends Cary needs to work to afford the shoes
    result = weekends_needed
    return result

print(solution())