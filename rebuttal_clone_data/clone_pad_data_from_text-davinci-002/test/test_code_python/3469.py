def solution():
    total_rows = 150
    seats_per_row = 10
    ticket_price = 10
    seats_not_taken = total_rows * seats_per_row * 0.2
    seats_taken = total_rows * seats_per_row - seats_not_taken
    money_earned = seats_taken * ticket_price
    result = money_earned
    return result

print(solution())