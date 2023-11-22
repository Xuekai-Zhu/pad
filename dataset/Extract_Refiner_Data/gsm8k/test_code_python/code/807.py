def solution():
    
    # Define the cost per branch and the total earnings from climbing
    COST_PER_BRANCH = 0.25
    TOTAL_EARNED = 105

    # Calculate the number of branches Felix needs to climb per day
    branches_per_day = TOTAL_EARNED / COST_PER_BRANCH

    # Display the number of branches Felix needs to climb per day
    result = branches_per_day
    return result

print(solution())