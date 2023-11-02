def solution():
    """Three times as many children as adults attend a concert on Saturday. An adult ticket costs $7 and a child's ticket costs $3. The theater collected a total of $6,000. How many people bought tickets?"""
    # Define the cost of an adult ticket and a child's ticket
    ADULT_TICKET_PRICE = 7
    CHILD_TICKET_PRICE = 3

    # Define the total amount collected
    total_amount = 6000

    # Define the equation for the number of children in terms of the number of adults
    # Three times as many children as adults attend the concert
    # C = 3A
    # C = number of children
    # A = number of adults
    # Since we want to solve for the number of adults, we need to rearrange the equation to be in terms of A:
    # A = C/3

    # Let's substitute this back into the equation for the total amount collected:
    # Total amount = (number of adult tickets sold x cost per adult ticket) + (number of child tickets sold x cost per child ticket)
    # Total amount = (C/3) x 7 + C x 3
    # Total amount = 7/3 C + 3C
    # Total amount = 16/3 C

    # Now we can solve for the number of children:
    # 16/3 C = total amount
    # C = (3/16) total amount
    children = (3 / 16) * total_amount

    # Substitute this back into the equation for the number of adults:
    adults = children / 3

    # Total number of people who bought tickets
    total_people = children + adults

    # Display the total number of people who bought tickets
    result = total_people
    return result

print(solution())