def solution():
    """John's hair grows 1.5 inches every month.  Every time it gets to 9 inches long he cuts it down to 6 inches.  A haircut costs $45 and he gives a 20% tip.  How much does he spend on haircuts a year?"""
    # Define the cost of a single haircut and tip percentage
    HAIRCUT_COST = 45
    TIP_PERCENTAGE = 0.2

    # Initialize the length of John's hair and total cost of haircuts
    hair_length = 0
    total_cost = 0

    # Calculate the total cost of haircuts for a year
    for i in range(12):
        # Add 1.5 inches to hair length every month
        hair_length += 1.5
        
        # If hair length reaches 9 inches, cut it down to 6 inches
        if hair_length >= 9:
            hair_length = 6
            total_cost += HAIRCUT_COST * (1 + TIP_PERCENTAGE)

    # Display the total cost of haircuts for a year
    result = total_cost * 12
    return result

print(solution())