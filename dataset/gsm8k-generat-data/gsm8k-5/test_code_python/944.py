def solution():
    kylie_daisies = 5  # Kylie starts with 5 daisies
    sister_daisies = 9  # Kylie's sister gives her 9 more daisies

    # Calculate the total number of daisies Kylie has now
    total_daisies = kylie_daisies + sister_daisies

    # Calculate the number of daisies Kylie gives to her mother
    daisies_given_away = total_daisies / 2

    # Calculate the number of daisies Kylie has left
    remaining_daisies = total_daisies - daisies_given_away
    result = remaining_daisies
    return result

print(solution())