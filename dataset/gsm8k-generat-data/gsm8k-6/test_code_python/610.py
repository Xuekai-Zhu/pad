def solution():
    total_pies = 2000
    pies_with_forks = 0.68 * total_pies  # calculate the number of pies eaten with forks
    pies_without_forks = total_pies - pies_with_forks  # calculate the number of pies not eaten with forks
    result = pies_without_forks
    return result

print(solution())