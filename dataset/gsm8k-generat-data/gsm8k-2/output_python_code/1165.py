def solution():
    """A gecko eats 70 crickets every three days. The first day she eats 30% of the crickets. The second day she eats 6 less than the first, and the third day she finishes up the remaining crickets. How many crickets does she eat on the third day?"""
    total_crickets = 70
    first_day_crickets = total_crickets * 0.3
    second_day_crickets = first_day_crickets - 6
    third_day_crickets = total_crickets - first_day_crickets - second_day_crickets
    result = third_day_crickets
    return result

print(solution())