def solution():
    """At the Bertolli Farm, they grow 2073 tomatoes, 4112 cobs of corn, and 985 onions. How many fewer onions are grown than tomatoes and corn together?"""
    tomatoes_corn_sum = 2073 + 4112
    onion_diff = tomatoes_corn_sum - 985
    result = onion_diff
    return result

print(solution())