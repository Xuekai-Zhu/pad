def solution():
    # Define the initial number of seagulls
    initial_seagulls = 36

    # Calculate the number of seagulls scared away by the kids
    scared_seagulls = initial_seagulls * (1/4)

    # Calculate the number of remaining seagulls
    remaining_seagulls = initial_seagulls - scared_seagulls

    # Calculate the number of seagulls that fly to McDonald's
    flown_seagulls = remaining_seagulls * (1/3)

    # Calculate the number of seagulls left on the roof
    seagulls_left = remaining_seagulls - flown_seagulls

    result = seagulls_left
    return result

print(solution())