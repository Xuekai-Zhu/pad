def solution():
    total_pies = 2000
    percent_with_forks = 0.68

    # Calculate the number of pies eaten with forks
    num_pies_with_forks = total_pies * percent_with_forks

    # Calculate the number of pies not eaten with forks
    num_pies_without_forks = total_pies - num_pies_with_forks
    result = num_pies_without_forks
    return result

print(solution())