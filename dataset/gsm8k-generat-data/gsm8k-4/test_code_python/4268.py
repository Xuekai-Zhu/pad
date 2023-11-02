def solution():
    """Derek has $40. He spends $14 on lunch for himself, $11 for lunch for his dad, and $5 on more lunch for himself. His brother Dave has $50 and only spends $7 on lunch for his mom. How much more money does Dave have left than Derek?"""
    # Calculate Derek's total spending
    derek_spending = 14 + 11 + 5

    # Calculate Derek's money left
    derek_money_left = 40 - derek_spending

    # Calculate Dave's money left
    dave_money_left = 50 - 7

    # Calculate the difference in money left between Dave and Derek
    difference = dave_money_left - derek_money_left

    # return the result
    result = difference
    return result

print(solution())