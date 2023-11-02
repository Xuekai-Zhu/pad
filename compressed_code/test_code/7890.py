def solution():
    
    total_oranges = 7 * 12
    oranges_reserved = total_oranges * (1/4)
    oranges_remaining = total_oranges - oranges_reserved
    oranges_sold_yesterday = oranges_remaining * (3/7)
    oranges_left = oranges_remaining - oranges_sold_yesterday - 4
    result = oranges_left
    return result

print(solution())