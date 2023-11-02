def solution():
    total_tickets = 24  # Mark and Sarah have a total of 24 traffic tickets
    sarah_speeding_tickets = 6  # Sarah has 6 speeding tickets
    mark_speeding_tickets = sarah_speeding_tickets  # Mark has an equal number of speeding tickets

    # Calculate the total number of parking tickets
    total_parking_tickets = total_tickets - sarah_speeding_tickets - mark_speeding_tickets

    # Calculate the number of parking tickets Mark has
    mark_parking_tickets = 2 * total_parking_tickets / 3
    result = mark_parking_tickets
    return result

print(solution())