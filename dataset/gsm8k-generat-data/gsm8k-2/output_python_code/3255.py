def solution():
    """Bert made 12 sandwiches for his trip. On the first day, he ate half of the sandwiches he made. The next day he ate 2 sandwiches less. How many sandwiches does Bert have left after these two days?"""
    sandwiches = 12
    eaten_first_day = sandwiches // 2
    eaten_second_day = eaten_first_day - 2
    remaining_sandwiches = sandwiches - eaten_first_day - eaten_second_day
    result = remaining_sandwiches
    return result

print(solution())