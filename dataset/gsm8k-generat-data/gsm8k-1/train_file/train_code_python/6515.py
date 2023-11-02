def solution():
    """Tate has 32 tickets for a particular game. He then buys two more tickets for the game. His friend Peyton, who has half as many total tickets, drives with him to the game. How many tickets do Tate and Peyton have together?"""
    tate_tickets = 32
    tate_tickets += 2
    peyton_tickets = tate_tickets / 2
    total_tickets = tate_tickets + peyton_tickets
    
    return total_tickets

print(solution())