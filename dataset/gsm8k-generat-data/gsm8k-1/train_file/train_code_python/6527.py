def solution():
    """At the Bertolli Farm, they grow 2073 tomatoes, 4112 cobs of corn, and 985 onions. How many fewer onions are grown than tomatoes and corn together?"""
    tomatoes = 2073
    corn = 4112
    onions = 985
    total_tomatoes_and_corn = tomatoes + corn
    difference = total_tomatoes_and_corn - onions
    result = difference
    return result

print(solution())