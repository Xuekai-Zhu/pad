def solution():
    """Darryl sells melons on the side of the road. He sells cantaloupes for $2 each and honeydews for $3.
    He started the day with 30 cantaloupes and 27 honeydews.
    He accidentally dropped a couple of cantaloupes and three of the honeydews turned out to be rotten.
    At the end of the day he had 8 cantaloupes and 9 honeydews left. How much money did he make?"""
    # Define the price of a cantaloupe and a honeydew
    CANTALOUPE_PRICE = 2
    HONEYDEW_PRICE = 3

    # Define the starting number of cantaloupes and honeydews
    starting_cantaloupes = 30
    starting_honeydews = 27

    # Define the number of cantaloupes and honeydews that were lost or went bad
    lost_cantaloupes = 2
    bad_honeydews = 3

    # Define the ending number of cantaloupes and honeydews
    ending_cantaloupes = 8
    ending_honeydews = 9

    # Calculate the total number of cantaloupes and honeydews sold
    sold_cantaloupes = starting_cantaloupes - lost_cantaloupes - ending_cantaloupes
    sold_honeydews = starting_honeydews - bad_honeydews - ending_honeydews

    # Calculate the total amount of money made
    total_money = sold_cantaloupes * CANTALOUPE_PRICE + sold_honeydews * HONEYDEW_PRICE

    # Display the total money made
    result = total_money
    return result

print(solution())