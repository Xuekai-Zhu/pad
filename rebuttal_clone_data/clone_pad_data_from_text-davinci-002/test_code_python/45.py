def solution():
    """It's Ava's birthday party. Her parents bought a unicorn piñata for $13 and filled it with all of her favorite treats. They bought 4 bags of Reese's for $9 per bag, 3 bags of Snickers for $5 per bag, and 5 bags of Skittles for $7 per bag. How much did the unicorn piñata and the treats cost altogether?"""
    unicorn_piñata = 13
    Reese's_bags = 4
    Reese's_price = 9
    Snickers_bags = 3
    Snickers_price = 5
    Skittles_bags = 5
    Skittles_price = 7
    total_cost = (Reese's_bags * Reese's_price) + (Snickers_bags * Snickers_price) + (Skittles_bags * Skittles_price) + unicorn_piñata
    result = total_cost
    return result

print(solution())