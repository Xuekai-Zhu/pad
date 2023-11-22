def solution():
    
    # Define the number of meatballs in each sub sandwich
    MEATBALLS_PER_SANDWICH = 4

    # Calculate the number of meatballs ordered by Sidney
    sidney_order = 10 - 3

    # Calculate the number of meatballs eaten by Mark
    mark_eaten = 4

    # Calculate the number of meatballs ordered by Sidney
    sidney_order = sidney_order - mark_eaten

    # Calculate the number of meatballs ordered by Sidney's sub sandwiches
    sidney_remaining = sidney_order + 3

    # Calculate the total number of meatballs remaining
    total_remaining = sidney_remaining + 3

    # Display the total number of meatballs remaining
    result = total_remaining
    return result

print(solution())