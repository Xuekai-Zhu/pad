def solution():
    starting_daisies = 5
    additional_daisies = 9

    # Calculate the total number of daisies Kylie has now
    total_daisies = starting_daisies + additional_daisies

    # Calculate the number of daisies Kylie gives to her mother
    daisies_given = total_daisies / 2

    # Calculate the number of daisies Kylie has left
    daisies_left = total_daisies - daisies_given
    result = daisies_left
    return result

print(solution())