def solution():
    stimulus_check = 2000
    wife_share = stimulus_check * 2/5
    remaining_amount = stimulus_check - wife_share

    first_son_share = remaining_amount * 2/5
    remaining_amount = remaining_amount - first_son_share

    second_son_share = remaining_amount * 40/100
    remaining_amount = remaining_amount - second_son_share

    savings_account = remaining_amount
    result = savings_account
    return result

print(solution())