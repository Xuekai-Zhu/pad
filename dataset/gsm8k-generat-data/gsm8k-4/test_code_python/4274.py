def solution():
    """After receiving the $2000 stimulus check, Mr. Eithan decided to share the amount with his family. He gave 2/5 of the amount to his wife, 2/5 of the remaining amount to his first son, 40% of the remaining amount to his second son, and kept the remaining in their family savings account. Calculate the total amount he kept in the family's savings account."""
    # Define the initial stimulus check amount
    stimulus_check = 2000

    # Calculate the amount given to Mr. Eithan's wife
    wife_share = stimulus_check * (2/5)

    # Calculate the remaining amount
    remaining_amount = stimulus_check - wife_share

    # Calculate the amount given to his first son
    first_son_share = remaining_amount * (2/5)

    # Calculate the remaining amount
    remaining_amount = remaining_amount - first_son_share

    # Calculate the amount given to his second son
    second_son_share = remaining_amount * 0.4

    # Calculate the amount kept in the family's savings account
    savings_account = remaining_amount - second_son_share

    # return the result
    result = savings_account
    return result

print(solution())