def solution():
    # Define the number of logs per tree for each type of tree
    pine_logs = 80
    maple_logs = 60
    walnut_logs = 100

    # Calculate the total number of logs for each type of tree
    total_pine_logs = pine_logs * 8
    total_maple_logs = maple_logs * 3
    total_walnut_logs = walnut_logs * 4

    # Calculate the total number of logs
    total_logs = total_pine_logs + total_maple_logs + total_walnut_logs
    result = total_logs
    return result

print(solution())