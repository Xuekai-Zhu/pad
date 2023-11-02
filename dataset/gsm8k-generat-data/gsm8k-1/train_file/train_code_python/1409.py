def solution():
    """Brittney can chop 15 onions in 5 minutes. Carl can chop 20 onions within that same time. How many more onions can Carl chop in 30 minutes than Brittney?"""
    onions_per_minute_brittney = 15 / 5
    onions_per_minute_carl = 20 / 5
    onions_chopped_brittney = onions_per_minute_brittney * 30
    onions_chopped_carl = onions_per_minute_carl * 30
    difference = onions_chopped_carl - onions_chopped_brittney
    result = difference
    return result

print(solution())