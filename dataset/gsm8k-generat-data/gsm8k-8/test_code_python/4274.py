def solution():
    stimulus_check = 2000
    wife_share = 2/5 * stimulus_check
    remaining_amount = stimulus_check - wife_share
    first_son_share = 2/5 * remaining_amount
    second_son_share = 0.4 * remaining_amount
    savings_account = remaining_amount - first_son_share - second_son_share
    result = savings_account
    return result

print(solution())