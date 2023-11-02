def solution():
    """Carl wants to buy a new coat that is quite expensive. He saved $25 each week for 6 weeks. On the seventh week, he had to use a third of his saving to pay some bills. On the eighth week, his dad gave him some extra money for him to buy his dream coat. If the coat cost $170, how much money did his dad give him?"""
    savings = 25 * 6
    savings -= savings / 3 # used 1/3 for bills
    remaining_savings = savings + 25 # savings from the 7th and 8th week
    dad_money = 170 - remaining_savings
    result = dad_money
    return result

print(solution())