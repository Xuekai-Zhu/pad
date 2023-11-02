def solution():
    """It's Ava's birthday party. Her parents bought a unicorn piñata for $13 and filled it with all of her favorite treats. They bought 4 bags of Reese's for $9 per bag, 3 bags of Snickers for $5 per bag, and 5 bags of Skittles for $7 per bag. How much did the unicorn piñata and the treats cost altogether?"""
    # Define the prices of the piñata and the treats
    pinata_price = 13
    reeses_price = 9
    snickers_price = 5
    skittles_price = 7

    # Calculate the total cost of the treats
    reeses_cost = 4 * reeses_price
    snickers_cost = 3 * snickers_price
    skittles_cost = 5 * skittles_price
    total_cost = reeses_cost + snickers_cost + skittles_cost

    # Add the cost of the piñata to the total cost
    total_cost += pinata_price

    # return the result
    result = total_cost
    return result

print(solution())