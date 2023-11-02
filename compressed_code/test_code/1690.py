def solution():
    
    total_funds = 10000
    friends_share = 0.4 * total_funds
    remaining_funds = total_funds - friends_share
    family_share = 0.3 * remaining_funds
    own_savings = remaining_funds - family_share
    result = own_savings
    return result

print(solution())