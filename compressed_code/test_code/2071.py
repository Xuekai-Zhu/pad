def solution():
    
    initial_oranges = 7 * 12
    friend_oranges = initial_oranges * (1/4)
    remaining_oranges = initial_oranges - friend_oranges
    sold_yesterday = remaining_oranges * (3/7)
    oranges_left = remaining_oranges - sold_yesterday - 4
    result = oranges_left
    return result

print(solution())