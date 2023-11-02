def solution():
    initial_seagulls = 36
    seagulls_scared_away = initial_seagulls * (1/4)
    seagulls_left = initial_seagulls - seagulls_scared_away
    seagulls_flown_away = seagulls_left * (1/3)
    final_seagulls = seagulls_left - seagulls_flown_away
    result = final_seagulls
    return result

print(solution())