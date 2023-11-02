def solution():
    """68% of all pies are eaten with forks. If there are 2000 pies of all kinds, how many of the pies are not eaten with forks?"""
    # Define the total number of pies and the percentage eaten with forks
    total_pies = 2000
    fork_percentage = 0.68

    # Calculate the number of pies eaten with forks
    fork_pies = total_pies * fork_percentage

    # Calculate the number of pies not eaten with forks
    non_fork_pies = total_pies - fork_pies

    result = non_fork_pies
    return result

print(solution())