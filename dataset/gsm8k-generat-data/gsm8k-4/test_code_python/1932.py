def solution():
    """To get admission into a school party, each football team member must pay $40. If there are 60 players on the football team and the entire team attends 8 such parties in a year, calculate the total amount of money collected in the 8 parties."""
    # Define the party admission fee and the number of football team members
    ADMISSION_FEE = 40
    NUM_MEMBERS = 60

    # Calculate the total amount of money collected in 8 parties
    total_collected = NUM_MEMBERS * ADMISSION_FEE * 8

    # Return the result
    result = total_collected
    return result

print(solution())