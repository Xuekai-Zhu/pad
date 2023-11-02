def solution():
    """At the beginning of the day there were 74 apples in a basket. If Ricki removes 14 apples and Samson removes twice as many as Ricki. How many apples are left in the basket by the end of the day?"""
    initial_apples = 74
    ricki_removed = 14
    samson_removed = ricki_removed * 2
    apples_left = initial_apples - ricki_removed - samson_removed
    result = apples_left
    return result

print(solution())