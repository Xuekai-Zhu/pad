def solution():
    """A bond paper ream has 500 sheets and costs $27. An office needs 5000 sheets of bond paper. How much will it cost to buy their needed sheets of paper?"""
    sheets_per_ream = 500
    price_per_ream = 27
    sheets_needed = 5000
    reams_needed = sheets_needed / sheets_per_ream
    total_cost = reams_needed * price_per_ream
    result = total_cost
    return result

print(solution())