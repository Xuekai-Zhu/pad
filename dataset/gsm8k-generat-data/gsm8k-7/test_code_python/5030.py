def solution():
    ticket_price = 3
    tickets_sold_per_minute = 5
    time_in_minutes = 6

    # Calculate the total number of tickets sold in 6 minutes
    total_tickets_sold = tickets_sold_per_minute * time_in_minutes

    # Calculate the total earnings from the tickets sold in 6 minutes
    total_earnings = total_tickets_sold * ticket_price
    result = total_earnings
    return result

print(solution())