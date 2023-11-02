def solution():
    """After receiving the $2000 stimulus check, Mr. Eithan decided to share the amount with his family. He gave 2/5 of the amount to his wife, 2/5 of the remaining amount to his first son, 40% of the remaining amount to his second son, and kept the remaining in their family savings account. Calculate the total amount he kept in the family's savings account."""
    
    stimulus_check = 2000
    wife_share = 2/5 * stimulus_check
    remaining_amount = stimulus_check - wife_share
    first_son_share = 2/5 * remaining_amount
    remaining_amount -= first_son_share
    second_son_share = 40/100 * remaining_amount
    remaining_amount -= second_son_share
    savings = remaining_amount
    
    return savings

print(solution())