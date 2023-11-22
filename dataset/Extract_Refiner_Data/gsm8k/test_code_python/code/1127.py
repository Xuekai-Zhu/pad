def solution():
    
    # Define the length of the tree and the percentage of logs that can be made
    tree_length = 80
    log_percentage = 0.8

    # Calculate the length of logs that can be made
    log_length = tree_length * log_percentage

    # Calculate the number of planks that can be made
    planks = log_length * 5

    # Calculate the total amount of money that John makes
    total_money = planks * 1.2

    # Display the total money
    result = total_money
    return result

print(solution())