def solution():
    """Two sisters go to the movies.  Movie tickets are $8 per person.  If the sisters brought $25 with them, how much change will they receive after buying the tickets?"""
    # Define the cost of each movie ticket
    TICKET_PRICE = 8

    # Define the amount of money the sisters brought with them
    money = 25

    # Calculate the cost of the tickets for both sisters
    ticket_cost = TICKET_PRICE * 2

    # Calculate the change the sisters will receive
    change = money - ticket_cost

    # Display the change the sisters will receive
    result = change
    return result

print(solution())