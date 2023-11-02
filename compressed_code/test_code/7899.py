def solution():
    
    tvs_at_store = 8
    tvs_at_online_store = tvs_at_store * 3
    total_tvs = 42
    tvs_at_auction_site = total_tvs - (tvs_at_store + tvs_at_online_store)
    result = tvs_at_auction_site
    return result

print(solution())