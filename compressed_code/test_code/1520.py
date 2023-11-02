def solution():
    
    total_oranges = 10 * 30
    rotten_oranges = 50
    good_oranges = total_oranges - rotten_oranges
    juice_oranges = 30
    sold_oranges = good_oranges - juice_oranges
    result = sold_oranges
    return result

print(solution())