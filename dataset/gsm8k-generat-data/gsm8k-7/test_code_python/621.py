def solution():
    num_seagulls = 36

    # Calculate the number of seagulls scared away by kids
    num_scared_away = num_seagulls * (1/4)

    # Calculate the number of seagulls remaining
    num_remaining = num_seagulls - num_scared_away

    # Calculate the number of seagulls that fly to McDonald's
    num_flying_away = num_remaining * (1/3)

    # Calculate the number of seagulls left on the Taco Bell roof
    num_left = num_remaining - num_flying_away
    result = num_left
    return result

print(solution())