def solution():
    total_apples = 60
    apples_given_to_zenny = 18
    apples_given_to_andrea = 6

    # Calculate the total number of apples given away
    total_apples_given_away = apples_given_to_zenny + apples_given_to_andrea

    # Calculate the number of apples that Yanna kept
    apples_kept = total_apples - total_apples_given_away
    result = apples_kept
    return result

print(solution())