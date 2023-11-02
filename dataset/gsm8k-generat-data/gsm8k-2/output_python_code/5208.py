def solution():
    """Samantha, Aira, and Joe received 6 rubber bands each after they divided their bands equally. If Samantha had 5 more bands than Aira and Aira had 1 fewer band than Joe, how many rubber bands did Aira have?"""
    total_bands = 18    # 6 bands for each person
    joe_bands = total_bands // 3
    aira_bands = joe_bands - 1
    samantha_bands = aira_bands + 5
    aira_bands_total = aira_bands
    result = aira_bands_total
    return result

print(solution())