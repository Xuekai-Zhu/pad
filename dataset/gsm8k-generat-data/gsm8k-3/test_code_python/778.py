def solution():
    """
    James buys $3000 worth of stuff from Amazon. He has to return a TV that cost $700 and a bike that cost $500.
    He also sells another bike that cost 20% more than the bike he returned for 80% of what he bought it for.
    He then buys a toaster for $100. How much is he out of pocket for everything?
    """
    # Define the initial cost of James' purchase
    initial_cost = 3000

    # Define the cost of the TV and bike he returned
    return_cost = 700 + 500

    # Calculate the price James sold his bike for
    sold_bike_cost = round(1.2 * 500 * 0.8, 2)

    # Define the cost of the toaster
    toaster_cost = 100

    # Calculate James' total cost
    total_cost = initial_cost - return_cost - sold_bike_cost + toaster_cost

    # Display James' out of pocket cost
    result = total_cost
    return result

print(solution())