def solution():
    oranges_picked_on_monday = 100
    oranges_picked_on_tuesday = oranges_picked_on_monday * 3
    oranges_picked_on_wednesday = oranges_picked_on_monday - 30
    total_oranges = oranges_picked_on_monday + oranges_picked_on_tuesday + oranges_picked_on_wednesday
    result = total_oranges
    
    return result

print(solution())