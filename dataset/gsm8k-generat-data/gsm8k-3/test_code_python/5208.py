def solution():
    """A group of people pays $720 for admission tickets to an amusement park. The price of an adult ticket is $15, and a child ticket is $8. There are 25 more adults than children. How many children are in the group?"""
    # Define the cost of an adult ticket and a child ticket
    ADULT_TICKET_PRICE = 15
    CHILD_TICKET_PRICE = 8

    # Define the total amount paid for admission tickets
    total_paid = 720

    # Define the difference in number of adults and children
    DIFFERENCE = 25

    # Set up a system of equations to solve for the number of adults and children
    # A + C = Total people
    # A - C = Difference
    # Solve for A and C
    # A = (Total people + Difference) / 2
    # C = (Total people - Difference) / 2
    total_people = 0
    adults = 0
    children = 0
    for i in range(1, 100):
        total_people = i
        adults = (total_people + DIFFERENCE) / 2
        children = (total_people - DIFFERENCE) / 2
        if adults * ADULT_TICKET_PRICE + children * CHILD_TICKET_PRICE == total_paid:
            break

    # Display the number of children in the group
    result = children
    return result

print(solution())