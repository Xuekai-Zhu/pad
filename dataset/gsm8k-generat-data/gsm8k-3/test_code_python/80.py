def solution():
    """Jennifer purchased 40 cans of milk at the store before meeting her classmate Mark, who was also buying milk. Jennifer bought 6 additional cans for every 5 cans Mark bought. If Mark purchased 50 cans, how many cans of milk did Jennifer bring home from the store?"""
    # Define the initial number of cans purchased by Jennifer
    jennifer_cans = 40

    # Define the number of cans purchased by Mark
    mark_cans = 50

    # Calculate the additional cans Jennifer bought for every 5 cans Mark bought
    additional_cans = (mark_cans / 5) * 6

    # Calculate the total number of cans purchased by Jennifer
    total_cans = jennifer_cans + additional_cans

    # Return the result
    result = total_cans
    return result

print(solution())