def solution():
    total_seats = 60000  # The stadium seats 60,000 fans
    sold_seats = int(total_seats * 0.75)  # 75% of the seats were sold
    actual_attendees = sold_seats - 5000  # 5000 fans stayed home
    result = actual_attendees
    return result

print(solution())