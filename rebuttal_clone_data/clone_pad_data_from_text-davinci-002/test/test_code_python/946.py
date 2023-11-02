def solution():
 
    total_tomatoes = 100
    first_pick = total_tomatoes / 4
    second_pick = 20
    third_pick = 2 * second_pick
    final_total = total_tomatoes - first_pick - second_pick - third_pick
 
    return final_total

print(solution())