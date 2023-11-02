def solution():
    roller_coaster_tickets = 5  # Janet needs 5 tickets to ride the roller coaster
    giant_slide_tickets = 3  # Janet needs 3 tickets to ride the giant slide
    roller_coaster_rides = 7  # Janet wants to ride the roller coaster 7 times
    giant_slide_rides = 4  # Janet wants to ride the giant slide 4 times

    # Calculate the total number of tickets Janet needs
    total_tickets = (roller_coaster_tickets * roller_coaster_rides) + (giant_slide_tickets * giant_slide_rides)
    result = total_tickets
    return result

print(solution())