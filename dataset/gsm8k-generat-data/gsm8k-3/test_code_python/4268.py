def solution():
    """Derek has $40. He spends $14 on lunch for himself, $11 for lunch for his dad, and $5 on more lunch for himself.
       His brother Dave has $50 and only spends $7 on lunch for his mom. How much more money does Dave have left than Derek?"""
    # Calculate Derek's total spending
    dereks_spending = 14 + 11 + 5

    # Calculate Dave's total spending
    daves_spending = 7

    # Calculate Derek's remaining money
    dereks_money = 40 - dereks_spending

    # Calculate Dave's remaining money
    daves_money = 50 - daves_spending

    # Calculate the difference
    difference = daves_money - dereks_money

    # Display the result
    result = difference
    return result

print(solution())