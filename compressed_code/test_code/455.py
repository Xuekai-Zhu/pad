def solution():
    
    initial_seagulls = 36
    scared_seagulls = initial_seagulls * 0.25
    remaining_seagulls = initial_seagulls - scared_seagulls
    flying_seagulls = remaining_seagulls * (1/3)
    final_seagulls = remaining_seagulls - flying_seagulls
    result = final_seagulls
    return result

print(solution())