def solution():
    """Between them, Mark and Sarah have 24 traffic tickets. 
    Mark has twice as many parking tickets as Sarah, and they each have an equal number of speeding tickets. 
    If Sarah has 6 speeding tickets, how many parking tickets does Mark have?"""
    sarah_speeding_tickets = 6
    mark_speeding_tickets = sarah_speeding_tickets
    total_speeding_tickets = sarah_speeding_tickets + mark_speeding_tickets
    
    total_tickets = 24
    total_parking_tickets = total_tickets - total_speeding_tickets
    mark_parking_tickets = total_parking_tickets / 3 * 2
    result = mark_parking_tickets
    return result

print(solution())