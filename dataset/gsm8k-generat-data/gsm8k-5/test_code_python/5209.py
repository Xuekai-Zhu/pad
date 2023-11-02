def solution():
    total_bands = 6 * 3  # Each received 6 rubber bands after dividing equally
    aira_bands = (total_bands - 5 - (total_bands / 3)) + 1  # Aira had 5 more bands than Samantha and 1 fewer band than Joe

    result = aira_bands
    return result

print(solution())