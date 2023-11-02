def solution():
    
    drops_per_liter = 5000
    liters_to_die = 3
    drops_to_die = drops_per_liter * liters_to_die
    drops_per_feed = 20
    num_feeds_to_die = drops_to_die / drops_per_feed
    result = num_feeds_to_die
    return result

print(solution())