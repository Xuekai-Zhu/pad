def solution():
    """68% of all pies are eaten with forks. If there are 2000 pies of all kinds, how many of the pies are not eaten with forks?"""
    # Define the percentage of pies eaten with forks
    FORK_PERCENTAGE = 0.68

    # Define the total number of pies
    total_pies = 2000

    # Calculate the number of pies eaten with forks
    fork_pies = total_pies * FORK_PERCENTAGE

    # Calculate the number of pies not eaten with forks
    non_fork_pies = total_pies - fork_pies

    # Display the number of pies not eaten with forks
    result = non_fork_pies
    return result

print(solution())