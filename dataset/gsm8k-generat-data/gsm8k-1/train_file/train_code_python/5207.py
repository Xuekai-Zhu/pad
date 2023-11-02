def solution():
    """A group of people pays $720 for admission tickets to an amusement park. The price of an adult ticket is $15, and a child ticket is $8. There are 25 more adults than children. How many children are in the group?"""
    total_cost = 720
    adult_ticket_price = 15
    child_ticket_price = 8
    adult_count = child_count + 25
    total_count = adult_count + child_count
    total_cost = (adult_count * adult_ticket_price) + (child_count * child_ticket_price)
    # Solve for child_count
    child_count = (total_cost - adult_count * adult_ticket_price) / child_ticket_price
    result = child_count
    return result

print(solution())