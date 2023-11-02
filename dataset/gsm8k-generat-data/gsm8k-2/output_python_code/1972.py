def solution():
    """Emily spent X dollars on Friday, twice that amount on Saturday, and then three times X on Sunday. Over the three days, she spent $120. What is the value of X, in dollars?"""
    total_spent = 120
    sunday_spent = 3 * x
    saturday_spent = 2 * friday_spent
    friday_spent = x
    total_spent = sunday_spent + saturday_spent + friday_spent
    x = total_spent / 6
    result = x
    return result

print(solution())