def solution():
    oranges_picked_by_George = 45
    apples_picked_by_George = oranges_picked_by_George + 5
    oranges_picked_by_Amelia = oranges_picked_by_George - 18
    apples_picked_by_Amelia = apples_picked_by_George - 15
    total_oranges = oranges_picked_by_George + oranges_picked_by_Amelia
    total_apples = apples_picked_by_George + apples_picked_by_Amelia
    total_fruits = total_oranges + total_apples
    return total_fruits

print(solution())