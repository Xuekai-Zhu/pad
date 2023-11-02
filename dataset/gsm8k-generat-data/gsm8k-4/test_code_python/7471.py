def solution():
    """Janet, a third grade teacher, is picking up the sack lunch order from a local deli for the field trip she is taking her class on. There are 35 children in her class, 5 volunteer chaperones, and herself. She she also ordered three additional sack lunches, just in case there was a problem. Each sack lunch costs $7. How much do all the lunches cost in total?"""
    # Define the number of students, chaperones, and additional lunches
    num_students = 35
    num_chaperones = 5
    num_additional_lunches = 3

    # Calculate the total number of lunches needed
    total_lunches = num_students + num_chaperones + 1 + num_additional_lunches

    # Calculate the total cost of the lunches
    total_cost = total_lunches * 7

    result = total_cost
    return result

print(solution())