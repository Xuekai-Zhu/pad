def solution():
    ticket_price = 10
    total_rows = 20
    seats_per_row = 10
    total_seats = total_rows * seats_per_row
    percent_sold = 75
    seats_sold = total_seats * (percent_sold / 100)
    total_earned = seats_sold * ticket_price
    result = total_earned
    return result

print(solution())