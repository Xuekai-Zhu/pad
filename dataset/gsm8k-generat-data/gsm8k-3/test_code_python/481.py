def solution():
    """Julia is performing in her high school musical this weekend and her family wants to come to the show. Tickets are $12 for adults and $10 for children. If her mom, dad, grandma, and three little sisters come to the show, how much will the total be for their tickets?"""
    # Define the ticket prices
    ADULT_TICKET_PRICE = 12
    CHILD_TICKET_PRICE = 10

    # Define the number of adults and children attending
    num_adults = 3
    num_children = 3

    # Calculate the total cost of the tickets
    total_cost = num_adults * ADULT_TICKET_PRICE + num_children * CHILD_TICKET_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())