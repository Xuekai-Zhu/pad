def solution():
    
    small_children_tickets = 53
    older_children_tickets = 35
    adult_tickets = 75
    senior_tickets = 37
    total_omelets = (small_children_tickets * 0.5) + (older_children_tickets * 1) + (adult_tickets * 2) + (senior_tickets * 1.5) + 25
    eggs_needed = total_omelets * 2
    result = eggs_needed
    return result

print(solution())