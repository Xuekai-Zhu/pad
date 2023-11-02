def solution():
    """Janet needs 5 tickets to ride the roller coaster and 3 tickets to ride the giant slide. How many tickets does she need to ride the roller coaster 7 times and the giant slide 4 times?"""
    coaster_tickets = 5
    slide_tickets = 3
    coaster_rides = 7
    slide_rides = 4
    total_coaster_tickets = coaster_tickets * coaster_rides
    total_slide_tickets = slide_tickets * slide_rides
    total_tickets = total_coaster_tickets + total_slide_tickets
    result = total_tickets
    return result

print(solution())