def solution():
    """The movie theater sold 18 more than three times the number of tickets to the horror movie as it did to the romance movie. If the theater sold 25 tickets to the romance movie, how many tickets did it sell to the horror movie?"""
    # Define the number of tickets sold to the romance movie
    romance_tickets = 25

    # Calculate the number of tickets sold to the horror movie
    horror_tickets = 3 * romance_tickets + 18

    # Display the number of tickets sold to the horror movie
    result = horror_tickets
    return result

print(solution())