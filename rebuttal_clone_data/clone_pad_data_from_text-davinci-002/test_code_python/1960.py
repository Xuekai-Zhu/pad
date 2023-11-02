def solution():
    total_bags = 10
    oranges_per_bag = 30
    total_oranges = total_bags * oranges_per_bag
    rotten_oranges = 50
    oranges_for_juice = 30
    oranges_to_sell = total_oranges - rotten_oranges - oranges_for_juice
    result = oranges_to_sell
    
    return result

print(solution())