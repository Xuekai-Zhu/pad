def solution():
    oranges_per_dozen = 12
    total_oranges = 7 * oranges_per_dozen
    reserved_oranges = total_oranges * (1/4)
    remaining_oranges = total_oranges - reserved_oranges
    oranges_sold_yesterday = remaining_oranges * (3/7)
    oranges_left = remaining_oranges - oranges_sold_yesterday - 4
    result = oranges_left
    return result

print(solution())