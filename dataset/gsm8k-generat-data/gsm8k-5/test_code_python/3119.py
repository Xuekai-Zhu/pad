def solution():
    cans = 60  # Nick has 60 cans
    space_per_can_compacted = 0.2 * 30  # After being compacted, each can takes up 20% of 30 square inches
    total_space_compacted = cans * space_per_can_compacted  # Total space taken up by all the compacted cans
    result = total_space_compacted
    return result

print(solution())