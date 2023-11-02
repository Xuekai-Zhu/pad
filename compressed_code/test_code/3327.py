def solution():
    
    stimulus = 2000
    wife_share = 2/5 * stimulus
    remaining = stimulus - wife_share
    first_son_share = 2/5 * remaining
    remaining -= first_son_share
    second_son_share = 0.4 * remaining
    savings = remaining - second_son_share
    result = savings
    return result

print(solution())