def solution():
    total_seats = 500
    seats_taken = total_seats * 2/5
    seats_broken = total_seats / 10
    seats_available = total_seats - seats_taken - seats_broken
    result = seats_available
    return result

print(solution())