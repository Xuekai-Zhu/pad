def solution():
    
    initial_seagulls = 36
    scared_seagulls = initial_seagulls * (1/4)
    remaining_seagulls = initial_seagulls - scared_seagulls
    flying_seagulls = remaining_seagulls * (1/3)
    seagulls_left = remaining_seagulls - flying_seagulls
    result = seagulls_left
    return result

print(solution())