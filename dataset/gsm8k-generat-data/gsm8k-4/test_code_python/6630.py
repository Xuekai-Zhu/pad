def solution():
    """If Lyn donates $240 to a private organization each year where 1/3 of it goes to the community pantry project, 1/2 goes to the local crisis fund, 1/4 of the remaining goes to livelihood project funds, and the rest is for contingency funds. How much goes to contingency fund?"""
    # Define the total amount donated
    total_donation = 240

    # Calculate the amount donated to the community pantry project
    community_pantry = total_donation * (1/3)

    # Calculate the amount donated to the local crisis fund
    local_crisis = total_donation * (1/2)

    # Calculate the remaining amount after donations to the pantry and crisis fund
    remaining_donation = total_donation - community_pantry - local_crisis

    # Calculate the amount donated to the livelihood project funds
    livelihood_funds = remaining_donation * (1/4)

    # Calculate the amount for contingency funds
    contingency_funds = total_donation - community_pantry - local_crisis - livelihood_funds

    # return the result
    result = contingency_funds
    return result

print(solution())