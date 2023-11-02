def solution():
    """A man eats 5 sandwiches per day, his wife eats 4 sandwiches per day, and their son eats 2 sandwiches per day. How many sandwiches does this family eat in one week?"""
    sandwiches_per_day = 5 + 4 + 2
    days_per_week = 7
    total_sandwiches = sandwiches_per_day * days_per_week
    result = total_sandwiches
    return result

print(solution())