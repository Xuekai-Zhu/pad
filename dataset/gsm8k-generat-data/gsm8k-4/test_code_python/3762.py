def solution():
    """Between them, Mark and Sarah have 24 traffic tickets. Mark has twice as many parking tickets as Sarah, and they each have an equal number of speeding tickets. If Sarah has 6 speeding tickets, how many parking tickets does Mark have?"""
    # Define the number of speeding tickets
    speeding_tickets = 6

    # Calculate the total tickets for Sarah
    sarah_tickets = speeding_tickets + speeding_tickets

    # Calculate the number of parking tickets for Mark
    mark_parking_tickets = sarah_tickets * 2

    # Calculate the total tickets for Mark
    mark_tickets = mark_parking_tickets + speeding_tickets

    # Calculate the total tickets for both
    total_tickets = sarah_tickets + mark_tickets

    # Calculate the number of parking tickets for Sarah
    sarah_parking_tickets = total_tickets // 2 - sarah_tickets

    # Return the result
    result = mark_parking_tickets
    return result

print(solution())