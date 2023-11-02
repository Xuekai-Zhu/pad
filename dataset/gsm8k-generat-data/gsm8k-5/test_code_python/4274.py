def solution():
    stimulus_check = 2000  # Mr. Eithan received a $2000 stimulus check
    wife_share = (2/5) * stimulus_check  # Mr. Eithan gave 2/5 of the amount to his wife
    remaining_amount = stimulus_check - wife_share  # Calculate the remaining amount

    first_son_share = (2/5) * remaining_amount  # Mr. Eithan gave 2/5 of the remaining amount to his first son
    remaining_amount = remaining_amount - first_son_share  # Calculate the remaining amount

    second_son_share = 0.4 * remaining_amount  # Mr. Eithan gave 40% of the remaining amount to his second son
    remaining_amount = remaining_amount - second_son_share  # Calculate the remaining amount

    # The remaining amount is kept in the family savings account
    amount_in_savings = remaining_amount
    result = amount_in_savings
    return result

print(solution())