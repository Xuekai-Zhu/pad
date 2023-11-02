def solution():
    """Beatrice is shopping for a new TV. First she looks at 8 TVs at one store in person. Then she looks at three times as many TVs at an online store. She looks at more TVs on an auction site online. If Beatrice looked at 42 TVs in all, how many did look at on the auction site?"""
    tvs_at_store = 8
    tvs_at_online_store = tvs_at_store * 3
    total_tvs = 42
    tvs_at_auction_site = total_tvs - (tvs_at_store + tvs_at_online_store)
    result = tvs_at_auction_site
    return result

print(solution())