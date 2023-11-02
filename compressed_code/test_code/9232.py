def solution():
    
    initial_pick = 400
    new_pick = (3/4) * initial_pick
    total_pick = initial_pick + new_pick
    remaining_pick = 600
    target_pick = (initial_pick + new_pick + remaining_pick) * 2
    result = target_pick
    return result

print(solution())