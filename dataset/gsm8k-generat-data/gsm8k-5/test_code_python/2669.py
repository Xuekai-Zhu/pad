def solution():
    store_tvs = 8  # Beatrice looked at 8 TVs at the store
    online_tvs = 3 * store_tvs  # Beatrice looked at three times as many TVs online
    total_tvs = 42  # Beatrice looked at 42 TVs in total

    # Calculate the number of TVs Beatrice looked at on the auction site
    auction_tvs = total_tvs - store_tvs - online_tvs
    result = auction_tvs
    return result

print(solution())