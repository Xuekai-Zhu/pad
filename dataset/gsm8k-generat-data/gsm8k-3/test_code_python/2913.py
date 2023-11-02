def solution():
    """There are one hundred tickets to be sold for a volleyball game. Andrea sold twice as many tickets as Jude while Sandra sold 4 more than half the number of tickets Jude sold. If Jude sold 16 tickets, how many tickets need to be sold?"""
    # Define the number of tickets Jude sold
    jude_tickets = 16

    # Calculate the number of tickets Andrea sold
    andrea_tickets = jude_tickets * 2

    # Calculate the number of tickets Sandra sold
    sandra_tickets = (jude_tickets / 2) + 4

    # Calculate the total number of tickets sold
    total_tickets = jude_tickets + andrea_tickets + sandra_tickets

    # Calculate the number of tickets that need to be sold
    remaining_tickets = 100 - total_tickets

    # Display the number of tickets that need to be sold
    result = remaining_tickets
    return result

print(solution())