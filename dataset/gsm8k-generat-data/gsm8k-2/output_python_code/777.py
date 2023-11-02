def solution():
    """James buys $3000 worth of stuff from Amazon. He has to return a TV that cost $700 and a bike that cost $500. He also sells another bike that cost 20% more than the bike he returned for 80% of what he bought it for. He then buys a toaster for $100. How much is he out of pocket for everything?"""
    initial_purchase = 3000
    tv_cost = 700
    bike_return = 500
    sold_bike_cost = 1.2 * bike_return * 0.8
    toaster_cost = 100
    total_spent = initial_purchase - tv_cost - bike_return + sold_bike_cost + toaster_cost
    result = total_spent
    return result

print(solution())