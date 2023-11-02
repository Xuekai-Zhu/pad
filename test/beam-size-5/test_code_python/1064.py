def solution():
    
    # Define the number of meatballs in one sub sandwich
    MEATBALLS_PER_SUB_SANDWICH = 4

    # Calculate the number of meatballs Sidney ordered
    sidney_ordered = 10 - 3

    # Calculate the number of meatballs Mark ate
    mark_ate = 4

    # Calculate the total number of meatballs
    total_meatballs = sidney_ordered + mark_ate + 3

    # Calculate the number of meatballs remaining
    remaining_meatballs = MEATBALLS_PER_SUB_SANDWICH - total_meatballs

    # Display the number of meatballs remaining
    result = remaining_meatballs
    return result

print(solution())