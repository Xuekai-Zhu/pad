def solution():
    # Calculate the total cost of the tickets for Mrs. Lopez and her family
    adult_tickets = 2  # Mrs. Lopez and her husband
    children_tickets = 3  # for her 3 children
    senior_tickets = 2  # for her parents
    total_cost = (adult_tickets * 11) + (children_tickets * 8) + (senior_tickets * 9)  # Total cost of tickets
    result = total_cost
    return result

print(solution())