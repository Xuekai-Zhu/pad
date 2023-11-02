def solution():
    """Jennifer purchased 40 cans of milk at the store before meeting her classmate Mark, who was also buying milk. Jennifer bought 6 additional cans for every 5 cans Mark bought. If Mark purchased 50 cans, how many cans of milk did Jennifer bring home from the store?"""
    # Define the initial number of cans Jennifer purchased
    jennifer_cans = 40

    # Define the ratio of Mark's purchase to Jennifer's additional purchase
    ratio = 5/6

    # Calculate how many additional cans Jennifer bought for Mark's purchase
    mark_additional = ratio * 50

    # Add the additional cans to Jennifer's initial purchase
    total_cans = jennifer_cans + mark_additional

    result = total_cans
    return result

print(solution())