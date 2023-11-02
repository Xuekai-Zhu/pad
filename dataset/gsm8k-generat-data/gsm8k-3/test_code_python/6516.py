def solution():
    """Tate has 32 tickets for a particular game. He then buys two more tickets for the game. His friend Peyton, who has half as many total tickets, drives with him to the game. How many tickets do Tate and Peyton have together?"""
    # Define Tate's initial number of tickets and the number he bought
    tate_tickets = 32
    tate_tickets += 2

    # Calculate Peyton's number of tickets
    peyton_tickets = tate_tickets / 2

    # Calculate the total number of tickets
    total_tickets = tate_tickets + peyton_tickets

    # Display the total number of tickets
    result = total_tickets
    return result

print(solution())