def solution():
    """James buys $3000 worth of stuff from Amazon. He has to return a TV that cost $700 and a bike that cost $500. He also sells another bike that cost 20% more than the bike he returned for 80% of what he bought it for. He then buys a toaster for $100. How much is he out of pocket for everything?"""
    initial_cost = 3000
    tv_cost = 700
    bike1_cost = 500
    bike2_cost = bike1_cost * 1.2
    bike2_sale_price = bike2_cost * 0.8
    toaster_cost = 100
    total_return = tv_cost + bike1_cost
    total_sale = bike2_sale_price
    total_cost = initial_cost - total_return + total_sale + toaster_cost
    result = total_cost
    return result

print(solution())