def solution():
    """Emily spent X dollars on Friday, twice that amount on Saturday, and then three times X on Sunday. Over the three days, she spent $120. What is the value of X, in dollars?"""
    total_spent = 120
    friday_spending = x
    saturday_spending = 2 * x
    sunday_spending = 3 * x
    total_spending = friday_spending + saturday_spending + sunday_spending
    x = (total_spending - total_spent) / 6
    result = x
    return result

print(solution())