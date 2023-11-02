def solution():
    """To win a brand new Bible at Tom Sawyer's Sunday school, a pupil has to win 10 yellow tickets; each yellow ticket is obtained by trading in 10 red tickets; each red ticket is obtained by trading in 10 blue tickets; and blue tickets are earned by memorizing two Bible verses. But rather than go to all that trouble, Tom Sawyer has traded various toys and treasures of his with his friends until he has gathered 8 yellow, 3 red, and 7 blue tickets. How many more blue tickets would he need to earn to win a new Bible?"""
    blue_tickets_per_verse = 1/2
    blue_tickets_per_red = 10
    blue_tickets_per_yellow = 100
    yellow_tickets_needed = 10
    red_tickets_needed = 10
    blue_tickets_needed = 10
    yellow_tickets_owned = 8
    red_tickets_owned = 3
    blue_tickets_owned = 7
    total_blue_tickets_owned = blue_tickets_per_yellow * yellow_tickets_owned + blue_tickets_per_red * red_tickets_owned + blue_tickets_owned
    blue_tickets_needed = blue_tickets_per_yellow * yellow_tickets_needed + blue_tickets_per_red * red_tickets_needed + blue_tickets_needed
    remaining_blue_tickets_needed = blue_tickets_needed - total_blue_tickets_owned
    result = remaining_blue_tickets_needed
    return result

print(solution())