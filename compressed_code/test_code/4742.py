def solution():
    
    total_seats = 150 * 10
    seats_taken = int(total_seats * 0.8)
    ticket_price = 10
    total_earnings = seats_taken * ticket_price
    result = total_earnings
    return result

print(solution())