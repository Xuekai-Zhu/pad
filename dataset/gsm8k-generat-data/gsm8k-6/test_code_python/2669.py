def solution():
    # Calculate the number of TVs Beatrice looked at on the online store
    online_TVs = 3 * 8  # Beatrice looked at three times as many TVs on the online store

    # Calculate the number of TVs Beatrice looked at on auction site
    auction_TVs = 42 - 8 - online_TVs  # Beatrice looked at 8 TVs in person and 3 times as many as that on the online store

    result = auction_TVs
    return result

print(solution())