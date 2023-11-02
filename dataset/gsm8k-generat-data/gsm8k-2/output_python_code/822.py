def solution():
    """At the beginning of the day there were 74 apples in a basket. If Ricki removes 14 apples and Samson removes twice as many as Ricki. How many apples are left in the basket by the end of the day?"""
    starting_apples = 74
    ricki_removes = 14
    samson_removes = 2 * ricki_removes
    remaining_apples = starting_apples - ricki_removes - samson_removes
    result = remaining_apples
    return result

print(solution())