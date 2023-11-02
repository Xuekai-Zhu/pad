def solution():
    
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