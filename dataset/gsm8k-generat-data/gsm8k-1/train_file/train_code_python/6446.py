def solution():
    """A fruit stand is selling apples for $2 each. Emmy has $200 while Gerry has $100. If they want to buy apples, how many apples can Emmy and Gerry buy altogether?"""
    apple_price = 2
    emmy_budget = 200
    gerry_budget = 100
    total_budget = emmy_budget + gerry_budget
    total_apples = total_budget // apple_price
    result = total_apples
    return result

print(solution())