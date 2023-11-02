def solution():
    
    store_tvs = 8
    online_tvs = 3 * store_tvs
    total_tvs = 42
    auction_tvs = total_tvs - store_tvs - online_tvs
    result = auction_tvs
    return result

print(solution())