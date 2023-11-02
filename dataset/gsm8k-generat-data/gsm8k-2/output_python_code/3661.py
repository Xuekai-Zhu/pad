def solution():
    """For a school fundraiser, Tory needs to sell 50 packs of cookies. So far, he has sold 12 packs to his grandmother, 7 packs to his uncle, and 5 packs to a neighbor. How many more packs of cookies does Tory need to sell?"""
    total_packs = 50
    sold_packs = 12 + 7 + 5
    remaining_packs = total_packs - sold_packs
    result = remaining_packs
    return result

print(solution())