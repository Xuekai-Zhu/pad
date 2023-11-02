def solution():
    """A movie ticket for an adult costs $8, and a child's ticket costs $3. One adult is taking a group of children to the movies. She has $35. How many children can she take with her to the movies?"""
    adult_ticket_price = 8
    child_ticket_price = 3
    total_money = 35
    max_children = (total_money - adult_ticket_price) / child_ticket_price
    result = int(max_children)
    return result

print(solution())