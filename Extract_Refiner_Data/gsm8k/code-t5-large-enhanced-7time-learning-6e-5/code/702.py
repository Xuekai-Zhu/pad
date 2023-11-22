def solution():
    
    # Define the goal amount and the amount raised in the first 3 hours
    GOAL_AMOUNT = 6300
    FIRST_3_HOURS_RAISED = 2100

    # Calculate the total amount raised during the first 3 hours
    total_raised = FIRST_3_HOURS_RAISED

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = GOAL_AMOUNT - total_raised

    # Calculate the number of hours needed to reach the remaining amount
    hours_needed = remaining_amount / (FIRST_3_HOURS_RAISED / FIRST_3_HOURS_RAISED)

    # Display the number of hours needed
    result = hours_needed
    return result

print(solution())