def solution():
    """Brittney can chop 15 onions in 5 minutes. Carl can chop 20 onions within that same time. How many more onions can Carl chop in 30 minutes than Brittney?"""
    brittney_onion_per_min = 15 / 5
    carl_onion_per_min = 20 / 5
    brittney_onion_in_30_min = brittney_onion_per_min * 30
    carl_onion_in_30_min = carl_onion_per_min * 30
    difference = carl_onion_in_30_min - brittney_onion_in_30_min
    result = difference
    return result

print(solution())