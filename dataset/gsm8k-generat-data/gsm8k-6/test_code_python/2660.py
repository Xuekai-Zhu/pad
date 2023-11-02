def solution():
    total_oranges = 7 * 12  # 7 dozen oranges
    reserved_oranges = total_oranges * (1/4)  # 1/4 reserved for friend
    remaining_oranges = total_oranges - reserved_oranges  # remaining oranges
    yesterday_sold = remaining_oranges * (3/7)  # 3/7 sold yesterday
    remaining_oranges_today = remaining_oranges - yesterday_sold - 4  # 4 rotten oranges
    result = remaining_oranges_today
    return result

print(solution())