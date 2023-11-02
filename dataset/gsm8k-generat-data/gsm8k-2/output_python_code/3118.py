def solution():
    """Nick has 60 cans. Each can takes up 30 square inches of space before being compacted and 20% of that amount after being compacted. How much space do all the cans take up after being compacted?"""
    num_cans = 60
    before_compaction = num_cans * 30
    after_compaction = before_compaction * 0.2
    result = after_compaction
    return result

print(solution())