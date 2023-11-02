def solution():
    """Beatrice is shopping for a new TV. First she looks at 8 TVs at one store in person. Then she looks at three times as many TVs at an online store. She looks at more TVs on an auction site online. If Beatrice looked at 42 TVs in all, how many did look at on the auction site?"""
    store_tvs = 8
    online_tvs = 3 * store_tvs
    total_tvs = 42
    auction_tvs = total_tvs - store_tvs - online_tvs
    result = auction_tvs
    return result

print(solution())