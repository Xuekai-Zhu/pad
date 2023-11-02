def solution():
    total_crane_goal = 1000
    alice_folds = total_crane_goal / 2 
    remaining_cranes = total_crane_goal - alice_folds
    friend_folds = remaining_cranes / 5
    cranes_left = total_crane_goal - alice_folds - friend_folds
    result = cranes_left
    return result

print(solution())