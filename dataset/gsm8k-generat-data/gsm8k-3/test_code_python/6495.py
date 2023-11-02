def solution():
    """Every tree that Bart cuts down gives him 75 pieces of firewood.  If he burns 5 logs a day from November 1 through February 28, how many trees will he need to cut down?"""
    # Define the number of days from November 1st to February 28th
    num_days = 120

    # Define the number of logs burned per day
    num_logs_per_day = 5

    # Calculate the total number of logs burned over the 120-day period
    total_logs_burned = num_days * num_logs_per_day

    # Calculate the number of trees needed to produce the required number of logs
    logs_per_tree = 75
    trees_needed = total_logs_burned / logs_per_tree

    # Display the number of trees needed
    result = trees_needed
    return result

print(solution())