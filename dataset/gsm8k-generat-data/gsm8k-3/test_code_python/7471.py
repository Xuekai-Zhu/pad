def solution():
    """Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?"""
    # Define the number of people for whom to order lunches
    NUM_CHILDREN = 35
    NUM_CHAPERONES = 5
    NUM_EXTRA_LUNCHES = 3
    NUM_PEOPLE = NUM_CHILDREN + NUM_CHAPERONES + 1 + NUM_EXTRA_LUNCHES

    # Define the cost per lunch
    LUNCH_COST = 7

    # Calculate the total cost of all the lunches
    total_cost = NUM_PEOPLE * LUNCH_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())