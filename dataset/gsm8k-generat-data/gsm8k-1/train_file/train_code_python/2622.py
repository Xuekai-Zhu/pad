def solution():
    """To win a brand new Bible at Tom Sawyer's Sunday school, a pupil has to win 10 yellow tickets; each yellow ticket is obtained by trading in 10 red tickets; each red ticket is obtained by trading in 10 blue tickets; and blue tickets are earned by memorizing two Bible verses. But rather than go to all that trouble, Tom Sawyer has traded various toys and treasures of his with his friends until he has gathered 8 yellow, 3 red, and 7 blue tickets. How many more blue tickets would he need to earn to win a new Bible?"""
    yellow_tickets = 8
    red_tickets = 3
    blue_tickets = 7
    blue_tickets_needed = (10 - yellow_tickets % 10) * 10 // 2 - red_tickets * 10 - blue_tickets
    result = blue_tickets_needed
    return result

print(solution())