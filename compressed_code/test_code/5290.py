def solution():
    
    total_seats = 500
    taken_seats = total_seats * 2/5
    broken_seats = total_seats * 1/10
    available_seats = total_seats - taken_seats - broken_seats
    result = available_seats
    return result

print(solution())