def solution():
    """Johnny is a dog walker. He can walk 3 dogs at once. He gets paid $15 for a 30-minute walk and $20 for a 60-minute walk. Johnny works for 4 hours per day. If he always walks the maximum number of dogs possible and 6 dogs have 60-minute walks per day, how much money does he make in a week where he works 5 days?"""
    dogs_per_walk = 3
    max_dogs_per_day = 3 * 2  # Johnny works 4 hours = 8 walks (4*2) a day
    walks_per_day = max_dogs_per_day // dogs_per_walk
    short_walk_price = 15    # $15 for a 30-minute walk
    long_walk_price = 20     # $20 for a 60-minute walk
    long_walks_per_day = 6
    total_short_walks = walks_per_day - long_walks_per_day
    total_long_walks = long_walks_per_day
    total_short_walks_price = total_short_walks * short_walk_price
    total_long_walks_price = total_long_walks * long_walk_price
    total_price = total_short_walks_price + total_long_walks_price
    weekly_price = total_price * 5
    result = weekly_price
    return result

print(solution())