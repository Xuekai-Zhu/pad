def solution():
    mark_tickets = 24
    sarah_tickets = mark_tickets / 2
    sarah_speeding_tickets = 6
    sarah_parking_tickets = sarah_tickets - sarah_speeding_tickets
    mark_parking_tickets = 2 * sarah_parking_tickets
    result = mark_parking_tickets
    
    return result

print(solution())