def solution():
    # Calculate the total space taken by all the cans before being compacted
    total_space = 60 * 30  # each can takes up 30 square inches of space before being compacted

    # Calculate the total space taken by all the cans after being compacted
    compacted_space = total_space * 0.2  # 20% of the space taken before being compacted
    result = compacted_space
    return result

print(solution())