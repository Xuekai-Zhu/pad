def solution():
    """Between them, Mark and Sarah have 24 traffic tickets. Mark has twice as many parking tickets as Sarah, and they each have an equal number of speeding tickets. If Sarah has 6 speeding tickets, how many parking tickets does Mark have?"""
    # Define the number of Sarah's speeding tickets
    sarah_speeding_tickets = 6

    # Calculate the total number of tickets
    total_tickets = 24

    # Calculate the number of Mark's parking tickets
    mark_parking_tickets = (total_tickets - sarah_speeding_tickets) / 3 * 2

    # Display the number of Mark's parking tickets
    result = mark_parking_tickets
    return result

print(solution())