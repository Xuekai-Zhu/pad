def solution():
    """A family of parents and a child go to the cinema. The cost of an adult ticket is $12 and a child ticket is $8. Then they buy 2 popcorns for $3 each. How many dollars do they pay in total?"""
    adult_ticket_cost = 12
    child_ticket_cost = 8
    num_adults = 2
    num_children = 1
    num_popcorns = 2
    popcorn_cost = 3
    total_ticket_cost = (adult_ticket_cost * num_adults) + (child_ticket_cost * num_children)
    total_popcorn_cost = num_popcorns * popcorn_cost
    total_cost = total_ticket_cost + total_popcorn_cost
    result = total_cost
    return result

print(solution())