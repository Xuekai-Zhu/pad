def solution():
    """1 chocolate bar costs $1.50 and can be broken into 3 sections to make 3 s'mores.  Ron is hosting a boy scout camp out in his backyard for 15 scouts.  He wants to make sure that there are enough chocolate bars for everyone to have 2 s'mores each.  How much will he spend on chocolate bars?"""
    # Define the cost per chocolate bar and the number of scouts
    COST_PER_BAR = 1.5
    NUM_SCOUTS = 15

    # Calculate the total number of s'mores needed
    num_smores = NUM_SCOUTS * 2

    # Calculate the total number of chocolate bars needed
    num_bars = num_smores / 3

    # Calculate the total cost of the chocolate bars
    total_cost = num_bars * COST_PER_BAR

    # Display the total cost
    result = total_cost
    return result

print(solution())