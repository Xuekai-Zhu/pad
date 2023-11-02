def solution():
    orange_trees = 10
    oranges_picked = orange_trees * 12
    oranges_packed = oranges_picked / 6
    weeks = 3
    days_in_week = 7 
    total_oranges_packed = oranges_packed * weeks * days_in_week
    money_earned = total_oranges_packed * 2
    result = money_earned
    return result

print(solution())