def solution():
    
    oranges = 40
    apples = 70
    sold_oranges = oranges / 4
    sold_apples = apples / 2
    remaining_oranges = oranges - sold_oranges
    remaining_apples = apples - sold_apples
    total_fruits = remaining_oranges + remaining_apples
    result = total_fruits
    return result

print(solution())