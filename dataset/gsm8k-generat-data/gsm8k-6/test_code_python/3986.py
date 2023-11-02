def solution():
    # Calculate the total number of sweets
    total_sweets = (48 * 4) + ((1/3) * (48 * 4))  # 48 children take 4 sweets each, and there is one-third of the original amount left

    # Calculate the original number of sweets in the pack
    original_sweets = total_sweets / (1 + (1/3))
    result = original_sweets
    return result

print(solution())