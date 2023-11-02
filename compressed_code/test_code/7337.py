def solution():
    
    bags = 10
    oranges_per_bag = 30
    total_oranges = bags * oranges_per_bag
    rotten_oranges = 50
    good_oranges = total_oranges - rotten_oranges
    oranges_for_juice = 30
    oranges_to_sell = good_oranges - oranges_for_juice
    result = oranges_to_sell
    return result

print(solution())