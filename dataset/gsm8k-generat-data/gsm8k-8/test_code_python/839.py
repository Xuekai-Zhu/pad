def solution():
    # Define the number of tickets sold for each price level
    small_children_tickets = 53
    older_children_tickets = 35
    adult_tickets = 75
    senior_tickets = 37

    # Define the number of omelets needed for each price level
    small_children_omelets = small_children_tickets * 0.5
    older_children_omelets = older_children_tickets * 1
    adult_omelets = adult_tickets * 2
    senior_omelets = senior_tickets * 1.5
    
    # Calculate the total number of omelets needed
    total_omelets = small_children_omelets + older_children_omelets + adult_omelets + senior_omelets
    
    # Add extra 25 omelets
    total_omelets += 25
    
    # Calculate the total number of eggs needed
    total_eggs = total_omelets * 2
    
    return total_eggs

print(solution())