def solution():
    
    
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