def solution():
    """Ten adults went to a ball game with eleven children. Adult tickets are $8 each and the total bill was $124. How many dollars is one child's ticket?"""
    num_adults = 10
    num_children = 11
    adult_ticket_price = 8
    total_bill = 124
    child_ticket_price = (total_bill - (num_adults * adult_ticket_price)) / num_children
    result = child_ticket_price
    return result

print(solution())