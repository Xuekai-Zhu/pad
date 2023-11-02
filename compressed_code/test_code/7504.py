def solution():
    
    initial_funds = 10000
    friends_percent = 0.4
    family_percent = 0.3
    friends_share = initial_funds * friends_percent
    remaining_funds = initial_funds - friends_share
    family_share = remaining_funds * family_percent
    savings = initial_funds - friends_share - family_share
    result = savings
    return result

print(solution())