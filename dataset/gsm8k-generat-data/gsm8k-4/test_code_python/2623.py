def solution():
    """To win a brand new Bible at Tom Sawyer's Sunday school, a pupil has to win 10 yellow tickets; each yellow ticket is obtained by trading in 10 red tickets; each red ticket is obtained by trading in 10 blue tickets; and blue tickets are earned by memorizing two Bible verses. But rather than go to all that trouble, Tom Sawyer has traded various toys and treasures of his with his friends until he has gathered 8 yellow, 3 red, and 7 blue tickets. How many more blue tickets would he need to earn to win a new Bible?"""
    # Define the number of tickets required to win a Bible
    BIBLE_TICKETS = 10

    # Define the conversion rates for each ticket type
    RED_PER_BLUE = 10
    YELLOW_PER_RED = 10
    BLUE_PER_VERSE = 2

    # Define the number of tickets Tom Sawyer has already collected
    yellow_tickets = 8
    red_tickets = 3
    blue_tickets = 7

    # Calculate the total number of yellow tickets with the current number of red tickets
    total_yellow_tickets = yellow_tickets + (red_tickets * YELLOW_PER_RED)

    # Calculate the total number of red tickets with the current number of blue tickets
    total_red_tickets = red_tickets + (blue_tickets // RED_PER_BLUE)

    # Calculate the total number of blue tickets with the current number of memorized Bible verses
    total_blue_tickets = blue_tickets + (total_red_tickets * RED_PER_BLUE * BLUE_PER_VERSE)

    # Calculate the number of additional blue tickets needed to win a Bible
    additional_blue_tickets = BIBLE_TICKETS * RED_PER_BLUE * BLUE_PER_VERSE - total_blue_tickets

    result = additional_blue_tickets
    return result

print(solution())