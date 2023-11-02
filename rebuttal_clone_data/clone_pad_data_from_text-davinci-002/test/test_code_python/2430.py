def solution():
    stimulus_amount = 2000
    amount_given_to_wife = stimulus_amount * 2/5
    remaining_amount = stimulus_amount - amount_given_to_wife
    amount_given_to_first_son = remaining_amount * 2/5
    remaining_amount = remaining_amount - amount_given_to_first_son
    amount_given_to_second_son = remaining_amount * 40/100
    remaining_amount = remaining_amount - amount_given_to_second_son
    amount_saved = remaining_amount
    result = amount_saved
    return result

print(solution())