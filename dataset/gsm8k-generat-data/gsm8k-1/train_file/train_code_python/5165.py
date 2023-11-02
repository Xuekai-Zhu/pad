def solution():
    """The movie theater sold 18 more than three times the number of tickets to the horror movie as it did to the romance movie. If the theater sold 25 tickets to the romance movie, how many tickets did it sell to the horror movie?"""
    romance_tickets = 25
    horror_tickets = 3 * romance_tickets + 18
    result = horror_tickets
    return result

print(solution())