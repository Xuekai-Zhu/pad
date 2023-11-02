def solution():
    seagulls = 36  # initial number of seagulls
    scared_away = seagulls * (1/4)   # number of seagulls scared away by the kids
    remaining_seagulls = seagulls - scared_away   # number of seagulls remaining
    fly_away = remaining_seagulls * (1/3)   # number of seagulls that fly away to McDonald's parking lot
    seagulls_left = remaining_seagulls - fly_away   # number of seagulls left
    result = seagulls_left
    return result

print(solution())