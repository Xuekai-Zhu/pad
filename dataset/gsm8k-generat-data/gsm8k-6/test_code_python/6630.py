def solution():
    # Calculate the amount of money going to the community pantry project
    community_pantry = (1/3) * 240  

    # Calculate the amount of money going to the local crisis fund
    local_fund = (1/2) * 240  

    # Calculate the amount of money remaining after the first two allocations
    remaining_fund = 240 - community_pantry - local_fund  

    # Calculate the amount of money going to livelihood project funds
    livelihood_fund = (1/4) * remaining_fund  

    # Calculate the amount of money going to contingency funds
    contingency_fund = remaining_fund - livelihood_fund  

    result = contingency_fund
    return result

print(solution())