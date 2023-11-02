def solution():
    """For a school fundraiser, Tory needs to sell 50 packs of cookies. So far, he has sold 12 packs to his grandmother, 7 packs to his uncle, and 5 packs to a neighbor. How many more packs of cookies does Tory need to sell?"""
    packs_needed = 50
    packs_sold = 12 + 7 + 5
    packs_remaining = packs_needed - packs_sold
    result = packs_remaining
    return result

print(solution())