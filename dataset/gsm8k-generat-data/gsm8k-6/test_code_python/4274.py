def solution():
    stimulus_check = 2000  # stimulus check amount received
    wife_share = (2/5) * stimulus_check  # amount given to wife
    remaining_amount_1 = stimulus_check - wife_share  # remaining amount after giving to wife
    son1_share = (2/5) * remaining_amount_1  # amount given to first son
    remaining_amount_2 = remaining_amount_1 - son1_share  # remaining amount after giving to first son
    son2_share = 0.4 * remaining_amount_2  # amount given to second son
    remaining_amount_3 = remaining_amount_2 - son2_share  # remaining amount kept in savings account

    result = remaining_amount_3
    return result

print(solution())