def solution():
    """Darryl sells melons on the side of the road. He sells cantaloupes for $2 each and honeydews for $3. He started the day with 30 cantaloupes and 27 honeydews. He accidentally dropped a couple of cantaloupes and three of the honeydews turned out to be rotten. At the end of the day he had 8 cantaloupes and 9 honeydews left. How much money did he make?"""
    # Define the prices of cantaloupes and honeydews
    CANTALOUPE_PRICE = 2
    HONEYDEW_PRICE = 3

    # Define the initial number of cantaloupes and honeydews
    initial_cantaloupes = 30
    initial_honeydews = 27

    # Define the number of cantaloupes dropped and honeydews that turned out to be rotten
    dropped_cantaloupes = 2
    rotten_honeydews = 3

    # Define the final number of cantaloupes and honeydews
    final_cantaloupes = 8
    final_honeydews = 9

    # Calculate the number of cantaloupes and honeydews sold
    sold_cantaloupes = initial_cantaloupes - dropped_cantaloupes - final_cantaloupes
    sold_honeydews = initial_honeydews - rotten_honeydews - final_honeydews

    # Calculate the total money made from selling cantaloupes and honeydews
    total_money = (sold_cantaloupes * CANTALOUPE_PRICE) + (sold_honeydews * HONEYDEW_PRICE)

    result = total_money
    return result

print(solution())