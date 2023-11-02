def solution():
    total_straws = 300
    adult_pigs_share = 3/5
    num_piglets = 20

    # Calculate the number of straws for adult pigs
    adult_pigs_straws = total_straws * adult_pigs_share

    # Calculate the total number of straws for piglets
    piglets_straws = total_straws - adult_pigs_straws

    # Calculate the number of straws each piglet ate
    straws_per_piglet = piglets_straws / num_piglets
    result = straws_per_piglet
    return result

print(solution())