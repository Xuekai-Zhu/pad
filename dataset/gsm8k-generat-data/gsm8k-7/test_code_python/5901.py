def solution():
    roller_coaster_tickets_per_ride = 5
    giant_slide_tickets_per_ride = 3
    roller_coaster_rides = 7
    giant_slide_rides = 4

    # Calculate the total number of tickets needed for all roller coaster rides
    total_roller_coaster_tickets = roller_coaster_tickets_per_ride * roller_coaster_rides

    # Calculate the total number of tickets needed for all giant slide rides
    total_giant_slide_tickets = giant_slide_tickets_per_ride * giant_slide_rides

    # Calculate the total number of tickets needed for all rides
    total_tickets_needed = total_roller_coaster_tickets + total_giant_slide_tickets
    result = total_tickets_needed
    return result

print(solution())