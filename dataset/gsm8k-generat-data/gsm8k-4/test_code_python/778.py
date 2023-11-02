def solution():
    """James buys $3000 worth of stuff from Amazon. He has to return a TV that cost $700 and a bike that cost $500. He also sells another bike that cost 20% more than the bike he returned for 80% of what he bought it for. He then buys a toaster for $100. How much is he out of pocket for everything?"""
    # Define the initial purchase amount
    initial_purchase = 3000

    # Calculate the refund amount for the returned TV and bike
    refund = 700 + 500

    # Calculate the selling price of the bike sold
    bike_sold = 1.2 * 500 * 0.8

    # Calculate the total cost of the purchases and refunds
    total_cost = initial_purchase - refund + bike_sold + 100

    result = total_cost
    return result

print(solution())