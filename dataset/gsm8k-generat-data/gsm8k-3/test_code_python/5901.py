def solution():
    """Janet needs 5 tickets to ride the roller coaster and 3 tickets to ride the giant slide. How many tickets does she need to ride the roller coaster 7 times and the giant slide 4 times?"""
    # Define the number of tickets needed to ride the roller coaster and the giant slide
    ROLLER_TICKETS = 5
    SLIDE_TICKETS = 3

    # Define the number of times Janet wants to ride the roller coaster and the giant slide
    roller_rides = 7
    slide_rides = 4

    # Calculate the total number of tickets needed
    total_tickets = roller_rides * ROLLER_TICKETS + slide_rides * SLIDE_TICKETS

    # Display the total number of tickets needed
    result = total_tickets
    return result

print(solution())