def solution():
    # Calculate the portion that goes to the community pantry project
    community_pantry = 240 * (1/3)

    # Calculate the portion that goes to the local crisis fund
    local_crisis_fund = 240 * (1/2)

    # Calculate the remaining amount
    remaining = 240 - community_pantry - local_crisis_fund

    # Calculate the portion that goes to the livelihood project funds
    livelihood_funds = remaining * (1/4)

    # Calculate the portion that goes to contingency funds
    contingency_funds = remaining - livelihood_funds
    result = contingency_funds
    return result

print(solution())