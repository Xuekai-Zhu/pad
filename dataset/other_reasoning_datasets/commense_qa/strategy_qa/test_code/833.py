def solution():
    # Define two movie descriptions
    superbad_description = "two nerds on a quest for love, victorious"
    social_network_description = "University Nerd becomes one of the most powerful people in the world"
    # Check if movie descriptions show nerds as the losers
    if "losers" in superbad_description or "losers" in social_network_description:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())