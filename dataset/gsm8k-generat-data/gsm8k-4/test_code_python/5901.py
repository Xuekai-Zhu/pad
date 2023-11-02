def solution():
    """Janet needs 5 tickets to ride the roller coaster and 3 tickets to ride the giant slide. How many tickets does she need to ride the roller coaster 7 times and the giant slide 4 times?"""
    # Define the number of times Janet will ride the roller coaster and the giant slide
    roller_coaster_rides = 7
    giant_slide_rides = 4

    # Define the number of tickets required for each ride
    roller_coaster_tickets = 5
    giant_slide_tickets = 3

    # Calculate the total number of tickets needed
    total_tickets = roller_coaster_rides * roller_coaster_tickets + giant_slide_rides * giant_slide_tickets

    # Return the result
    result = total_tickets
    return result

print(solution())