def solution():
    total_oranges = 7 * 12
    reserved_oranges = total_oranges / 4
    sold_oranges = (total_oranges - reserved_oranges) * (3 / 7)
    rotten_oranges = 4
    remaining_oranges = total_oranges - reserved_oranges - sold_oranges - rotten_oranges
    
    return remaining_oranges

print(solution())