def solution():
    """For a class fundraiser, 30 students were asked to bring in 12 brownies each. 20 students were asked to bring in 24 cookies each and 15 students were asked to bring in 12 donuts each. If they sell everything for $2.00 each, how much money will they raise?"""
    brownies = 30 * 12
    cookies = 20 * 24
    donuts = 15 * 12
    total_items = brownies + cookies + donuts
    price_per_item = 2
    total_fundraiser = total_items * price_per_item
    result = total_fundraiser
    return result

print(solution())