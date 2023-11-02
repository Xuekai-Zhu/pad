def solution():
    """Julia is performing in her high school musical this weekend and her family wants to come to the show. Tickets are $12 for adults and $10 for children. If her mom, dad, grandma, and three little sisters come to the show, how much will the total be for their tickets?"""
    # Define the number of adults and children
    num_adults = 3
    num_children = 3

    # Define the cost per ticket
    adult_ticket_price = 12
    child_ticket_price = 10

    # Calculate the total cost of tickets for Julia's family
    total_cost = (num_adults * adult_ticket_price) + (num_children * child_ticket_price)

    result = total_cost
    return result

print(solution())