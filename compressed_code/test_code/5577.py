def solution():
    
    calories_per_chip = 10
    chips_per_bag = 24
    bag_price = 2
    calories_needed = 480
    chips_needed = calories_needed / calories_per_chip
    bags_needed = chips_needed / chips_per_bag
    total_cost = bags_needed * bag_price
    result = total_cost
    return result

print(solution())