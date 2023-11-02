def solution():
    # Calculate the percentage of germs that would be killed by both sprays
    killed_by_both = 75  # 50% + (25% of the remaining 50%)
    remaining = 100 - killed_by_both  # percentage of germs still remaining
    result = remaining
    return result

print(solution())