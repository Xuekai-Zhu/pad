def solution():
    total_bands = 18  # 6 each for Samantha, Aira, and Joe
    aira_bands = (total_bands - 5) / 3  # Aira had 5 fewer bands than Samantha
    joe_bands = aira_bands + 1  # Aira had 1 fewer band than Joe
    result = aira_bands
    return result

print(solution())