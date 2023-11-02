def solution():
    """For a school fundraiser, Tory needs to sell 50 packs of cookies. So far, he has sold 12 packs to his grandmother, 7 packs to his uncle, and 5 packs to a neighbor. How many more packs of cookies does Tory need to sell?"""
    # Define the total number of packs Tory needs to sell
    TOTAL_PACKS = 50

    # Define the number of packs Tory has already sold
    sold_packs = 12 + 7 + 5

    # Calculate the number of packs Tory still needs to sell
    remaining_packs = TOTAL_PACKS - sold_packs

    # Display the number of remaining packs Tory needs to sell
    result = remaining_packs
    return result

print(solution())