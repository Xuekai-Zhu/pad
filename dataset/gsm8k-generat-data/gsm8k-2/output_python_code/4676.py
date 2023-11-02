def solution():
    """For a fundraiser, Nellie needs to sell 45 rolls of gift wrap. So far, she has sold 1 roll to her grandmother, 10 rolls to her uncle, and 6 rolls to a neighbor. How many more rolls of gift wrap does Nellie need to sell?"""
    total_gift_wrap = 45
    sold_gift_wrap = 1 + 10 + 6
    remaining_gift_wrap = total_gift_wrap - sold_gift_wrap
    result = remaining_gift_wrap
    return result

print(solution())