def solution():
    yellow_tickets = 8  # Tom has 8 yellow tickets
    red_tickets = 3  # Tom has 3 red tickets, which is equal to 30 blue tickets (10 red tickets per 1 yellow ticket)
    blue_tickets = 7 + (3 * 10)  # Tom has 7 blue tickets and he traded 3 red tickets for additional 30 blue tickets

    # Calculate how many more blue tickets Tom needs to win a Bible
    remaining_yellow_tickets = 10 - yellow_tickets % 10  # Tom needs 2 more yellow tickets to have 10, which is equal to 20 red tickets
    remaining_red_tickets = 10 - red_tickets % 10  # Tom needs 7 more red tickets to have 10, which is equal to 70 blue tickets
    remaining_blue_tickets = remaining_yellow_tickets * 10 * 2 + remaining_red_tickets * 10  # Tom needs this many blue tickets

    result = remaining_blue_tickets
    return result

print(solution())