def solution():
    num_paychecks = 26
    personal_contribution = 100.0
    match_percentage = 0.06

    # Calculate Holly's total personal contribution in one year
    total_personal = num_paychecks * personal_contribution

    # Calculate the total company contribution in one year based on Holly's personal contribution
    total_match = total_personal * match_percentage

    # Calculate the total amount contributed to Holly's 401k account in one year
    total_contributed = total_personal + total_match
    result = total_contributed
    return result

print(solution())