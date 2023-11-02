def solution():
    """To win a brand new Bible at Tom Sawyer's Sunday school, a pupil has to win 10 yellow tickets; each yellow ticket is obtained by trading in 10 red tickets; each red ticket is obtained by trading in 10 blue tickets; and blue tickets are earned by memorizing two Bible verses. But rather than go to all that trouble, Tom Sawyer has traded various toys and treasures of his with his friends until he has gathered 8 yellow, 3 red, and 7 blue tickets. How many more blue tickets would he need to earn to win a new Bible?"""
    # Define the number of tickets needed to win a new Bible
    BIBLE_TICKETS = 10

    # Define the number of tickets required to trade up to each color
    YELLOW_TICKETS = 10
    RED_TICKETS = 10
    BLUE_VERSES = 2

    # Define the number of tickets Tom already has
    yellow_tickets = 8
    red_tickets = 3
    blue_tickets = 7

    # Calculate the total number of blue tickets Tom needs to win a new Bible
    total_blue_tickets = BIBLE_TICKETS * YELLOW_TICKETS * RED_TICKETS * BLUE_VERSES - \
                         yellow_tickets * YELLOW_TICKETS * RED_TICKETS * BLUE_VERSES - \
                         red_tickets * RED_TICKETS * BLUE_VERSES - blue_tickets * 1

    # Display the number of blue tickets Tom still needs to win a new Bible
    result = total_blue_tickets
    return result

print(solution())