def solution():
    """Nick has 60 cans. Each can takes up 30 square inches of space before being compacted and 20% of that amount after being compacted. How much space do all the cans take up after being compacted?"""
    num_cans = 60
    space_per_can = 30
    compacted_space_percentage = 20
    compacted_space = space_per_can * (compacted_space_percentage / 100)
    total_compacted_space = num_cans * compacted_space
    result = total_compacted_space
    return result

print(solution())