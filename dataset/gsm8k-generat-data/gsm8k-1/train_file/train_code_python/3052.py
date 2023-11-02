def solution():
    """Carl wants to buy a new coat that is quite expensive. He saved $25 each week for 6 weeks. On the seventh week, he had to use a third of his saving to pay some bills. On the eighth week, his dad gave him some extra money for him to buy his dream coat. If the coat cost $170, how much money did his dad give him?"""
    savings_per_week = 25
    weeks_saved = 6
    total_savings = savings_per_week * weeks_saved
    savings_spent = total_savings / 3
    total_savings -= savings_spent
    coat_cost = 170
    money_needed = coat_cost - total_savings
    result = money_needed
    return result

print(solution())