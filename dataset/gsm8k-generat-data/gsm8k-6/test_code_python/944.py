def solution():
    # Calculate the number of daisies Kylie has after her sister gives her more
    kylie_daisies = 5 + 9  # Kylie starts with 5, and gets 9 more from her sister
    kylie_daisies /= 2  # Kylie gives half of her daisies to her mother
    remaining_daisies = kylie_daisies  # Kylie is left with the remaining daisies
    result = remaining_daisies
    return result

print(solution())