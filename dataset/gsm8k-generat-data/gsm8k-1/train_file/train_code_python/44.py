def solution():
    """It's Ava's birthday party. Her parents bought a unicorn piñata for $13 and filled it with all of her favorite treats. They bought 4 bags of Reese's for $9 per bag, 3 bags of Snickers for $5 per bag, and 5 bags of Skittles for $7 per bag. How much did the unicorn piñata and the treats cost altogether?"""
    pinata_cost = 13
    reese_bags = 4
    reese_cost_per_bag = 9
    snickers_bags = 3
    snickers_cost_per_bag = 5
    skittles_bags = 5
    skittles_cost_per_bag = 7
    
    total_treats_cost = (reese_bags * reese_cost_per_bag) + (snickers_bags * snickers_cost_per_bag) + (skittles_bags * skittles_cost_per_bag)
    total_cost = pinata_cost + total_treats_cost
    
    result = total_cost
    return result

print(solution())