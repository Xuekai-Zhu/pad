def solution():
    """Mrs. Lopez and her family are going to the movie theatre.  Adult tickets are $11.  Children’s tickets (ages 3-12) are $8.  Senior citizen’s tickets (ages 60+) are $9.  Mrs. Lopez needs to buy movie tickets for her husband, herself, her parents (ages 72 and 75), and her three children (ages 7, 10, 14).  How much money does she need to buy everyone’s tickets?"""
    # Define the prices for each type of ticket
    ADULT_PRICE = 11
    CHILD_PRICE = 8
    SENIOR_PRICE = 9

    # Define the number of each type of ticket needed
    adult_tickets = 2
    child_tickets = 3
    senior_tickets = 2

    # Calculate the total cost for each type of ticket
    adult_cost = adult_tickets * ADULT_PRICE
    child_cost = child_tickets * CHILD_PRICE
    senior_cost = senior_tickets * SENIOR_PRICE

    # Calculate the total cost for all tickets
    total_cost = adult_cost + child_cost + senior_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())