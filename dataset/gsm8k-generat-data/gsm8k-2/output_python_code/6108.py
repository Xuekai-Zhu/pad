def solution():
    """Dr. Harry wants to know how many candies Susan consumed during the week.
    Susan tells him she bought 3 on Tuesday, 5 on Thursday, 2 on Friday.
    If she has only 4 of them left, how many did she eat?"""
    total_candies = 3 + 5 + 2 + 4
    consumed_candies = total_candies - 4
    result = consumed_candies
    return result

print(solution())