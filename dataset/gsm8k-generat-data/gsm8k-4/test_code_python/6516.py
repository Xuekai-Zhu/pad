def solution():
    """Tate has 32 tickets for a particular game. He then buys two more tickets for the game. His friend Peyton, who has half as many total tickets, drives with him to the game. How many tickets do Tate and Peyton have together?"""
    # Define the initial number of tickets Tate has
    tate_tickets = 32

    # Add the two tickets he buys
    tate_tickets += 2

    # Calculate the total number of tickets between Tate and Peyton
    total_tickets = tate_tickets + (tate_tickets / 2)

    # return the result
    result = total_tickets
    return result

print(solution())