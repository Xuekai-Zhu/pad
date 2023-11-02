def solution():
    """It's Ava's birthday party. Her parents bought a unicorn piñata for $13 and filled it with all of her favorite treats. They bought 4 bags of Reese's for $9 per bag, 3 bags of Snickers for $5 per bag, and 5 bags of Skittles for $7 per bag. How much did the unicorn piñata and the treats cost altogether?"""
    # Define the prices of the piñata and the treats
    pinata_cost = 13
    reeses_cost = 9
    snickers_cost = 5
    skittles_cost = 7

    # Calculate the total cost of the treats
    reeses_total = 4 * reeses_cost
    snickers_total = 3 * snickers_cost
    skittles_total = 5 * skittles_cost
    treats_total = reeses_total + snickers_total + skittles_total

    # Calculate the total cost of the piñata and the treats
    total_cost = pinata_cost + treats_total

    result = total_cost
    return result

print(solution())