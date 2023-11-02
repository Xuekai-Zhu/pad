def solution():
    """After receiving the $2000 stimulus check, Mr. Eithan decided to share the amount with his family. He gave 2/5 of the amount to his wife, 2/5 of the remaining amount to his first son, 40% of the remaining amount to his second son, and kept the remaining in their family savings account. Calculate the total amount he kept in the family's savings account."""
    # Define the amount of the stimulus check
    stimulus_check = 2000

    # Calculate the amount given to Mr. Eithan's wife
    wife_amount = (2 / 5) * stimulus_check

    # Calculate the remaining amount after giving to Mr. Eithan's wife
    remaining_amount = stimulus_check - wife_amount

    # Calculate the amount given to Mr. Eithan's first son
    first_son_amount = (2 / 5) * remaining_amount

    # Calculate the remaining amount after giving to Mr. Eithan's first son
    remaining_amount = remaining_amount - first_son_amount

    # Calculate the amount given to Mr. Eithan's second son
    second_son_amount = 0.4 * remaining_amount

    # Calculate the remaining amount after giving to Mr. Eithan's second son
    remaining_amount = remaining_amount - second_son_amount

    # Calculate the amount kept in the family's savings account
    savings_amount = remaining_amount

    # Display the amount kept in the family's savings account
    result = savings_amount
    return result

print(solution())