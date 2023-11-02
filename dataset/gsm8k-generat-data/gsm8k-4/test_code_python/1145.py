def solution():
    """Daria wants to go to a concert by her favorite band. She wants to buy tickets for her and 
    for three of her friends. One ticket cost is $90. How much money does Daria need 
    to earn if she currently has only $189?"""
    # Define the cost of one ticket and the number of tickets needed
    ticket_cost = 90
    num_tickets = 4

    # Calculate the total cost of the tickets
    total_cost = ticket_cost * num_tickets

    # Calculate the amount of money Daria needs to earn
    money_needed = total_cost - 189

    result = money_needed
    return result

print(solution())