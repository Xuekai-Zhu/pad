def solution():
    """The music festival of Bassompierre begins tonight with a concert by the string orchestra "PIANISSIMO". The ticket price for adults is $26; for children, the price is half. The show starts at 9 pm and goes very well. At about 11:00 pm, the concert organizer made his accounts. There were 183 adults and 28 children who attended the show. What was the total revenue of the concert?"""
    # Define the ticket price for adults and children
    ADULT_TICKET_PRICE = 26
    CHILD_TICKET_PRICE = ADULT_TICKET_PRICE / 2

    # Get the number of adults and children who attended the show
    num_adults = 183
    num_children = 28

    # Calculate the total revenue from adult ticket sales
    adult_revenue = num_adults * ADULT_TICKET_PRICE

    # Calculate the total revenue from child ticket sales
    child_revenue = num_children * CHILD_TICKET_PRICE

    # Calculate the total revenue from all ticket sales
    total_revenue = adult_revenue + child_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())