def solution():
    # Calculate the number of tickets Amanda has sold so far
    sold_tickets = 5*4 + 32  # on the first day, she sells 5 friends 4 tickets each, on the second day she sells 32 tickets

    # Calculate the number of tickets Amanda still needs to sell
    remaining_tickets = 80 - sold_tickets

    # Calculate the number of tickets Amanda needs to sell on the third day
    third_day_tickets = remaining_tickets / 2  # she has one more day to sell the remaining tickets
    result = third_day_tickets
    return result

print(solution())