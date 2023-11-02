def solution():
    """Samantha, Aira, and Joe received 6 rubber bands each after they divided their bands equally. If Samantha had 5 more bands than Aira and Aira had 1 fewer band than Joe, how many rubber bands did Aira have?"""
    total_bands = 6 * 3
    aira_bands = (total_bands - 1 - 5) / 3
    result = aira_bands
    return result

print(solution())