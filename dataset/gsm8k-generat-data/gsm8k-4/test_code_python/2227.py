def solution():
    """Russel and Jen went to the circus. Jen played a shooting game twice, while Russel rode the carousel three times. If the shooting game costs 5 tickets and the carousel costs 3 tickets. How many tickets did they use?"""
    # Define the cost of the shooting game and the carousel
    shooting_cost = 5
    carousel_cost = 3

    # Calculate the total number of tickets used by Jen
    jen_tickets = shooting_cost * 2

    # Calculate the total number of tickets used by Russel
    russel_tickets = carousel_cost * 3

    # Calculate the total number of tickets used by both of them
    total_tickets = jen_tickets + russel_tickets

    # return the result
    result = total_tickets
    return result

print(solution())