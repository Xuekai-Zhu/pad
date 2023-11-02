def solution():
    # Find the total number of blue tickets he already has
    blue_tickets_already_owned = 7

    # Find the total number of red tickets he already has
    red_tickets_already_owned = 3

    # Find the total number of yellow tickets he already has
    yellow_tickets_already_owned = 8

    # Calculate the total number of blue tickets needed to win the Bible
    blue_tickets_needed = 10 * 10 * 10 - yellow_tickets_already_owned * 10 - red_tickets_already_owned * 10 - blue_tickets_already_owned * 2

    result = blue_tickets_needed
    return result

print(solution())