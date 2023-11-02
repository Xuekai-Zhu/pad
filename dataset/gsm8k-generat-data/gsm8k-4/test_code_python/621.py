def solution():
    """There are 36 seagulls on the roof of the Taco Bell. Kids scare 1/4 of them away by throwing stones, and 1/3 of the remaining birds decide to fly to McDonald's parking lot. How many seagulls are left?"""
    # Define the initial number of seagulls
    initial_seagulls = 36

    # Calculate the number of seagulls scared away by the kids
    scared_away = initial_seagulls * (1/4)

    # Calculate the number of remaining seagulls
    remaining_seagulls = initial_seagulls - scared_away

    # Calculate the number of seagulls that fly to McDonald's parking lot
    fly_away = remaining_seagulls * (1/3)

    # Calculate the number of seagulls left on the roof
    seagulls_left = remaining_seagulls - fly_away

    result = seagulls_left
    return result

print(solution())