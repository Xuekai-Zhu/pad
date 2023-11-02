def solution():
    # Calculate the total number of speeding tickets
    total_speeding_tickets = 6 * 2

    # Calculate Sarah's parking tickets
    sarah_parking_tickets = (24 - total_speeding_tickets) / 3

    # Calculate Mark's parking tickets
    mark_parking_tickets = sarah_parking_tickets * 2

    result = mark_parking_tickets
    return result

print(solution())