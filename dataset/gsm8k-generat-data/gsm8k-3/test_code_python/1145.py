def solution():
    """Daria wants to go to a concert by her favorite band. She wants to buy tickets for her and for three of her friends. One ticket cost is $90. How much money does Daria need to earn if she currently has only $189?"""
    # Define the cost of one ticket
    TICKET_PRICE = 90

    # Define the number of tickets Daria needs to buy
    num_tickets = 4

    # Calculate the total cost of the tickets
    total_cost = num_tickets * TICKET_PRICE

    # Calculate how much more money Daria needs to earn
    extra_money = total_cost - 189

    # Display how much extra money Daria needs to earn
    result = extra_money
    return result

print(solution())