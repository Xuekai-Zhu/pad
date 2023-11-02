def solution():
    small_children_tickets = 53
    older_children_tickets = 35
    adult_tickets = 75
    senior_tickets = 37
    num_extra_omelets = 25

    # Calculate the total number of omelets needed
    total_omelets = (small_children_tickets * 0.5) + older_children_tickets + (adult_tickets * 2) + (senior_tickets * 1.5) + num_extra_omelets

    # Calculate the total number of eggs needed
    total_eggs = total_omelets * 2
    result = total_eggs
    return result

print(solution())