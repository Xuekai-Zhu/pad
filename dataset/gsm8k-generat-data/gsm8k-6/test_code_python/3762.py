def solution():
    # Calculate the total number of tickets for Sarah
    total_tickets_sarah = 6 + 6  # Sarah has 6 speeding tickets and an equal number of parking tickets

    # Calculate the total number of parking tickets for Mark
    parking_tickets_mark = 24/3 - total_tickets_sarah  # Mark has twice as many parking tickets as Sarah, and they have an equal number of speeding tickets

    result = parking_tickets_mark
    return result

print(solution())