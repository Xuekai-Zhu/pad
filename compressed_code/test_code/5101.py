def solution():
    
    total_seats = 8 * 12
    allowed_seats_per_row = 8 * 0.75
    total_allowed_seats = allowed_seats_per_row * 12
    unoccupied_seats = total_seats - total_allowed_seats
    result = unoccupied_seats
    return result

print(solution())