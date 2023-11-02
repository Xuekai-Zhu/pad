def solution():
    
    initial_pick = 400
    second_pick = 3/4 * initial_pick
    remaining_pick = 600
    total_pick_needed = initial_pick + second_pick + remaining_pick
    target_pick = total_pick_needed * 2
    result = target_pick
    return result

print(solution())