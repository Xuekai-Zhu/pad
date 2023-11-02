def solution():
    total_tickets = 80  # Amanda has to sell 80 tickets in 3 days
    sold_on_first_day = 5 * 4  # Amanda sold 5 friends 4 tickets each on first day
    sold_on_second_day = 32  # Amanda sold 32 tickets on the second day

    # Calculate the total tickets sold so far
    total_sold = sold_on_first_day + sold_on_second_day

    # Calculate the tickets Amanda needs to sell on the third day to meet her goal
    required_tickets = total_tickets - total_sold
    result = required_tickets
    return result

print(solution())