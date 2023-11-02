def solution():
    """For a school fundraiser, Tory needs to sell 50 packs of cookies. So far, he has sold 12 packs to his grandmother, 7 packs to his uncle, and 5 packs to a neighbor. How many more packs of cookies does Tory need to sell?"""
    # Define the target number of packs to sell and the number of packs sold so far
    target_packs = 50
    sold_packs = 12 + 7 + 5

    # Calculate the number of packs left to sell
    packs_left = target_packs - sold_packs

    # Return the result
    result = packs_left
    return result

print(solution())