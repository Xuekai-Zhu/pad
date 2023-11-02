def solution():
    """Calculate how many eggs the Rotary Club needs to buy for their Omelet Breakfast fundraiser"""
    # Define the number of tickets sold in each category
    small_children_tickets = 53
    older_children_tickets = 35
    adult_tickets = 75
    senior_tickets = 37

    # Define the number of omelets each category will eat
    small_children_omelets = small_children_tickets * 0.5
    older_children_omelets = older_children_tickets * 1
    adult_omelets = adult_tickets * 2
    senior_omelets = senior_tickets * 1.5

    # Calculate the total number of omelets needed
    total_omelets = small_children_omelets + older_children_omelets + adult_omelets + senior_omelets + 25

    # Calculate the number of eggs needed
    eggs_needed = 2 * total_omelets

    # Display the number of eggs needed
    result = eggs_needed
    return result

print(solution())