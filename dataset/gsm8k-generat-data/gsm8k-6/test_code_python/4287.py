def solution():
    # Calculate the total number of parsley sprigs used
    used_sprigs = 8 + (12/2)  # 8 plates with one whole sprig and 12 plates with 1/2 sprig each
    remaining_sprigs = 25 - used_sprigs  # Calculate the remaining sprigs
    result = remaining_sprigs
    return result

print(solution())